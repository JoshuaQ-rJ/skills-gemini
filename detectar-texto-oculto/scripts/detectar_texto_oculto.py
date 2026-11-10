#!/usr/bin/env python3
"""Detecta texto oculto o invisible en PDFs (posible inyeccion de instrucciones para agentes de IA).

Uso:
    python detectar_texto_oculto.py archivo.pdf [otro.pdf ...] [--json] [--visible salida.txt]

Requiere: pip install pymupdf
"""
import argparse
import json
import re
import sys
import unicodedata

try:
    import pymupdf as fitz
except ImportError:  # versiones antiguas
    import fitz

PALABRAS_SOSPECHOSAS = re.compile(
    r"\b(ignor\w*|instrucci\w*|instruction\w*|prompt|ia\b|ai\b|chatgpt|claude|gemini|copilot|antigravity|"
    r"modelo de lenguaje|language model|llm|agente|agent|si eres|if you are|you must|debes|incluye|include|"
    r"menciona|mention|responde|answer|escribe|write|no (le )?digas|do not tell|system)\b",
    re.IGNORECASE,
)

ZERO_WIDTH = {"​", "‌", "‍", "⁠", "﻿", "­", "᠎"}
BIDI = {chr(c) for c in range(0x202A, 0x202F)} | {chr(c) for c in range(0x2066, 0x206A)}


def es_tag_unicode(ch):
    return 0xE0000 <= ord(ch) <= 0xE007F


def caracteres_raros(texto):
    hallados = []
    for ch in texto:
        if ch in ZERO_WIDTH or ch in BIDI or es_tag_unicode(ch):
            hallados.append(f"U+{ord(ch):04X} {unicodedata.name(ch, '?')}")
    return hallados


def decodificar_tags(texto):
    """Los caracteres 'tag' (U+E0020-U+E007E) pueden esconder ASCII invisible."""
    oculto = "".join(chr(ord(c) - 0xE0000) for c in texto if 0xE0020 <= ord(c) <= 0xE007E)
    return oculto


def contraste_region(pix, rect, escala):
    """Desviacion de los pixeles en la caja del texto. ~0 = no deja huella visible."""
    x0 = max(int(rect.x0 * escala), 0)
    y0 = max(int(rect.y0 * escala), 0)
    x1 = min(int(rect.x1 * escala), pix.width - 1)
    y1 = min(int(rect.y1 * escala), pix.height - 1)
    if x1 <= x0 or y1 <= y0:
        return None
    vals = []
    paso_x = max((x1 - x0) // 40, 1)
    paso_y = max((y1 - y0) // 10, 1)
    n = pix.n
    for y in range(y0, y1 + 1, paso_y):
        for x in range(x0, x1 + 1, paso_x):
            p = pix.pixel(x, y)
            vals.append(sum(p[:3]) / 3 if n >= 3 else p[0])
    if not vals:
        return None
    media = sum(vals) / len(vals)
    return (sum((v - media) ** 2 for v in vals) / len(vals)) ** 0.5


def analizar_pdf(ruta):
    doc = fitz.open(ruta)
    hallazgos = []
    texto_visible = []

    def agregar(pagina, motivo, texto, extra=None):
        texto = texto.strip()
        if not texto:
            return
        h = {"pagina": pagina, "motivo": motivo, "texto": texto[:500]}
        if PALABRAS_SOSPECHOSAS.search(texto):
            h["parece_instruccion"] = True
        if extra:
            h.update(extra)
        hallazgos.append(h)

    escala = 2.0
    for num, page in enumerate(doc, start=1):
        rect_pag = page.rect
        pix = page.get_pixmap(matrix=fitz.Matrix(escala, escala), alpha=False)
        visibles_pag = []
        try:
            trazas = page.get_texttrace()
        except Exception:
            trazas = []
        for sp in trazas:
            texto = "".join(chr(c[0]) for c in sp.get("chars", []) if c[0] > 0)
            if len(texto.strip()) <= 2:  # signos sueltos (−, puntos) dan falsos positivos
                continue
            bbox = fitz.Rect(sp["bbox"])
            motivos = []
            if sp.get("type") == 3:
                motivos.append("modo de dibujo invisible (render mode 3)")
            if sp.get("opacity", 1) is not None and sp.get("opacity", 1) < 0.15:
                motivos.append(f"opacidad {sp.get('opacity'):.2f}")
            if sp.get("size", 12) < 2:
                motivos.append(f"letra diminuta ({sp.get('size'):.2f} pt)")
            if not bbox.intersects(rect_pag):
                motivos.append("fuera de la pagina")
            elif not motivos:
                c = contraste_region(pix, bbox & rect_pag, escala)
                if c is not None and c < 2.0:
                    color = sp.get("color")
                    motivos.append(
                        "no deja huella visible (mismo color que el fondo o tapado)"
                        + (f", color {tuple(round(x, 2) for x in color)}" if color else "")
                    )
            if motivos:
                agregar(num, "; ".join(motivos), texto)
            else:
                visibles_pag.append(texto)

        texto_pag = page.get_text()
        raros = caracteres_raros(texto_pag)
        if raros:
            oculto = decodificar_tags(texto_pag)
            agregar(num, "caracteres invisibles de Unicode: " + ", ".join(sorted(set(raros))[:8]),
                    oculto or texto_pag[:200])

        for annot in page.annots() or []:
            contenido = (annot.info or {}).get("content", "")
            if contenido:
                agregar(num, f"anotacion ({annot.type[1]})", contenido)
        for w in page.widgets() or []:
            if w.field_value:
                agregar(num, f"campo de formulario '{w.field_name}'", str(w.field_value))

        texto_visible.append(f"--- Pagina {num} ---\n" + "".join(visibles_pag))

    # capas opcionales apagadas
    try:
        for xref, info in (doc.get_ocgs() or {}).items():
            if not info.get("on", True):
                hallazgos.append({"pagina": None, "motivo": "capa oculta en el PDF", "texto": info.get("name", "")})
    except Exception:
        pass

    for clave, valor in (doc.metadata or {}).items():
        if valor and PALABRAS_SOSPECHOSAS.search(str(valor)):
            agregar(None, f"metadatos ({clave})", str(valor))

    try:
        nombres = doc.embfile_names() if doc.embfile_count() else []
        raros = [n for n in nombres if not re.fullmatch(r"equation-\d+\.xml", n)]
        if raros:
            hallazgos.append({"pagina": None, "motivo": "archivos incrustados", "texto": ", ".join(raros)})
    except Exception:
        pass

    try:
        js = doc.get_js() if hasattr(doc, "get_js") else None
        if js:
            agregar(None, "JavaScript en el PDF", str(js))
    except Exception:
        pass

    return {"archivo": ruta, "paginas": len(doc), "hallazgos": hallazgos, "texto_visible": "\n".join(texto_visible)}


def analizar_docx(ruta):
    """Word: texto marcado como oculto (w:vanish), blanco, diminuto o con caracteres invisibles."""
    import zipfile
    import html

    hallazgos = []
    with zipfile.ZipFile(ruta) as z:
        partes = [n for n in z.namelist() if re.match(r"word/(document|header\d*|footer\d*|footnotes|comments)\.xml", n)]
        visibles = []
        for parte in partes:
            xml = z.read(parte).decode("utf-8", "ignore")
            for run in re.findall(r"<w:r[ >].*?</w:r>", xml, re.S):
                texto = html.unescape("".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", run, re.S)))
                if not texto.strip():
                    continue
                motivos = []
                if re.search(r"<w:vanish/>|<w:vanish w:val=\"(1|true)\"", run):
                    motivos.append("marcado como texto oculto")
                if re.search(r"<w:color w:val=\"(FFFFFF|ffffff)\"", run):
                    motivos.append("letra blanca")
                m = re.search(r"<w:sz w:val=\"(\d+)\"", run)
                if m and int(m.group(1)) < 4:
                    motivos.append(f"letra diminuta ({int(m.group(1)) / 2} pt)")
                raros = caracteres_raros(texto)
                if raros:
                    motivos.append("caracteres invisibles de Unicode")
                    texto = decodificar_tags(texto) or texto
                if motivos:
                    h = {"pagina": parte, "motivo": "; ".join(motivos), "texto": texto[:500]}
                    if PALABRAS_SOSPECHOSAS.search(texto):
                        h["parece_instruccion"] = True
                    hallazgos.append(h)
                else:
                    visibles.append(texto)
    return {"archivo": ruta, "paginas": len(partes), "hallazgos": hallazgos, "texto_visible": "".join(visibles)}


def analizar(ruta):
    return analizar_docx(ruta) if ruta.lower().endswith(".docx") else analizar_pdf(ruta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="+", help="archivos .pdf o .docx")
    ap.add_argument("--json", action="store_true", help="salida en JSON")
    ap.add_argument("--visible", help="guarda aqui solo el texto visible (del primer archivo)")
    args = ap.parse_args()

    resultados = [analizar(p) for p in args.pdfs]
    if args.visible:
        with open(args.visible, "w", encoding="utf-8") as f:
            f.write(resultados[0]["texto_visible"])
    if args.json:
        for r in resultados:
            r.pop("texto_visible", None)
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
        return
    for r in resultados:
        print(f"\n=== {r['archivo']} ({r['paginas']} paginas) ===")
        if not r["hallazgos"]:
            print("Sin texto oculto detectado.")
            continue
        for h in r["hallazgos"]:
            marca = "  <-- PARECE INSTRUCCION PARA IA" if h.get("parece_instruccion") else ""
            pag = f"p. {h['pagina']}" if h["pagina"] else "documento"
            print(f"[{pag}] {h['motivo']}{marca}\n    \"{h['texto']}\"")
    sys.exit(1 if any(r["hallazgos"] for r in resultados) else 0)


if __name__ == "__main__":
    main()
