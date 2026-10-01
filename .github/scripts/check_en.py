"""Comprueba que la versión en inglés sigue a la española.

El castellano es la fuente; el inglés, su traducción. Las dos tienen que tener la misma estructura: los
mismos títulos, bloques de código y filas de tabla, en el mismo número. Si alguien cambia una y se olvida de
la otra, esto falla y dice qué par se ha separado.

Uso: python3 .github/scripts/check_en.py
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[2]
PARES = [
    ("README.md", "README.en.md"),
    ("guia-cowork.md", "en/guide-cowork.md"),
    ("guia-claude-code.md", "en/guide-claude-code.md"),
    ("casos-de-uso.md", "en/use-cases.md"),
    ("prompts/01-inicial-cowork.md", "en/prompts/01-initial-cowork.md"),
    ("prompts/02-inicial-claude-code.md", "en/prompts/02-initial-claude-code.md"),
    ("prompts/03-crecimiento.md", "en/prompts/03-growth.md"),
    ("prompts/04-hooks-claude-code.md", "en/prompts/04-hooks-claude-code.md"),
    ("prompts/05-bitacora.md", "en/prompts/05-handoff.md"),
]


def huella(texto):
    titulos = codigo = filas = 0
    en_codigo = False
    for linea in texto.splitlines():
        if linea.startswith("```"):
            codigo += 1
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        if re.match(r"#{1,6} ", linea):
            titulos += 1
        elif linea.lstrip().startswith("|"):
            filas += 1
    return {"títulos": titulos, "bloques de código": codigo // 2, "filas de tabla": filas}


def main():
    fallos = 0
    for es, en in PARES:
        p_es, p_en = RAIZ / es, RAIZ / en
        if not p_en.exists():
            print(f"FALTA  {en} (traducción de {es})")
            fallos += 1
            continue
        h_es, h_en = huella(p_es.read_text(encoding="utf-8")), huella(p_en.read_text(encoding="utf-8"))
        if h_es != h_en:
            fallos += 1
            dif = ", ".join(f"{k}: {h_es[k]} frente a {h_en[k]}" for k in h_es if h_es[k] != h_en[k])
            print(f"DESFASE {es} <-> {en} — {dif}")
        else:
            print(f"OK     {es} <-> {en}")
    if fallos:
        print(f"\n{fallos} par(es) por poner al día: el inglés tiene que seguir al castellano.")
        sys.exit(1)


if __name__ == "__main__":
    main()
