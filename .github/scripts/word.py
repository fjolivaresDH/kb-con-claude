"""Genera las dos guías en Word a partir de los Markdown del repositorio.

Uso: python3 .github/scripts/word.py <versión>
Deja en dist/ Guia-KB-Cowork-v<versión>.docx y Guia-KB-ClaudeCode-v<versión>.docx.
Necesita pandoc en el PATH.
"""
import datetime
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

WEB = "https://fjolivaresdh.github.io/kb-con-claude"
RAIZ = pathlib.Path(__file__).resolve().parents[2]
DIST = RAIZ / "dist"
TMP = RAIZ / "dist" / "tmp"


def enlaces_a_la_web(md):
    """Los enlaces a otros .md del repo no sirven dentro de un Word: apuntan a la web."""
    def cambio(m):
        ruta, ancla = m.group(1), m.group(2) or ""
        ruta = re.sub(r"^(\.\./)+", "", ruta)
        return f"]({WEB}/{ruta}.html{ancla})"
    md = re.sub(r"\]\((?!https?:|#)([^)#]+?)\.md(#[^)]*)?\)", cambio, md)
    return md.replace("](LICENSE)", f"]({WEB}/LICENSE)")


def con_version(md, version, fecha):
    """Línea de versión justo debajo del título."""
    titulo, resto = md.split("\n", 1)
    return f"{titulo}\n\n*Versión {version} · {fecha}*\n{resto}"


def anexo_prompts(nombres):
    partes = ["\n\n## Anexo — los prompts\n\n"
              "Los mismos prompts de la guía, para copiarlos sin salir del documento.\n"]
    for n in nombres:
        texto = (RAIZ / "prompts" / n).read_text(encoding="utf-8")
        texto = re.sub(r"^# ", "### ", texto, count=1)
        partes.append("\n" + texto)
    return "".join(partes)


def documento_de_referencia():
    """La plantilla de estilos de pandoc, con el código a 7,5 pt: las líneas del prompt rondan
    los 95 caracteres y a tamaño normal se parten."""
    ref = TMP / "ref.docx"
    with open(ref, "wb") as f:
        subprocess.run(["pandoc", "-o", "-", "--print-default-data-file", "reference.docx"],
                       stdout=f, check=True)
    salida = TMP / "ref-ajustada.docx"
    with zipfile.ZipFile(ref) as zin, zipfile.ZipFile(salida, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            datos = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                xml = datos.decode("utf-8")
                for estilo in ("SourceCode", "VerbatimChar"):
                    xml = ajustar_tamano(xml, estilo, 15)
                datos = xml.encode("utf-8")
            zout.writestr(item, datos)
    return salida


def ajustar_tamano(xml, estilo, medios_puntos):
    patron = re.compile(r'(<w:style\b[^>]*w:styleId="%s"[^>]*>)(.*?)(</w:style>)' % estilo, re.S)
    m = patron.search(xml)
    if not m:
        return xml
    cuerpo = re.sub(r"<w:szCs?\b[^>]*/>", "", m.group(2))
    sz = f'<w:sz w:val="{medios_puntos}"/><w:szCs w:val="{medios_puntos}"/>'
    if "<w:rPr>" in cuerpo:
        cuerpo = cuerpo.replace("</w:rPr>", sz + "</w:rPr>", 1)
    elif "<w:rPr/>" in cuerpo:
        cuerpo = cuerpo.replace("<w:rPr/>", f"<w:rPr>{sz}</w:rPr>", 1)
    else:
        cuerpo += f"<w:rPr>{sz}</w:rPr>"
    return xml[:m.start()] + m.group(1) + cuerpo + m.group(3) + xml[m.end():]


def generar(fuente, destino, version, fecha, ref, anexo=""):
    md = (RAIZ / fuente).read_text(encoding="utf-8")
    md = con_version(enlaces_a_la_web(md + anexo), version, fecha)
    tmp = TMP / fuente
    tmp.write_text(md, encoding="utf-8")
    subprocess.run(["pandoc", str(tmp), "-f", "gfm", "-o", str(DIST / destino),
                    "--reference-doc", str(ref), "--resource-path", str(RAIZ)], check=True)
    print("OK", DIST / destino)


def main():
    version = sys.argv[1]
    fecha = datetime.date.today().strftime("%d/%m/%Y")
    shutil.rmtree(DIST, ignore_errors=True)
    TMP.mkdir(parents=True)
    ref = documento_de_referencia()
    generar("guia-cowork.md", f"Guia-KB-Cowork-v{version}.docx", version, fecha, ref)
    generar("guia-claude-code.md", f"Guia-KB-ClaudeCode-v{version}.docx", version, fecha, ref,
            anexo_prompts(["02-inicial-claude-code.md", "03-crecimiento.md",
                           "04-hooks-claude-code.md", "05-bitacora.md"]))
    shutil.rmtree(TMP)


if __name__ == "__main__":
    main()
