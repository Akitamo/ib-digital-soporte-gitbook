"""Valida la sección Personas antes de subir cambios.

Comprueba:
  1. Menú (SUMMARY): todas las páginas están y todas las entradas existen; título = H1.
  2. Enlaces internos, anclas, imágenes, bloques reutilizables y variables.
  3. Bloques GitBook abiertos y cerrados (tabs, stepper, hint, content-ref, details).
  4. Índice de contenidos: cada página está en el índice y viceversa; las anclas de «resuelve»
     existen; cada tarea con faq_tema incluye su bloque faq-<tema>.
  5. Bloques de preguntas frecuentes al día con el índice (generar_faq.py).
  6. Catálogo de enlaces contextuales: las anclas fijas existen.

Uso: python herramientas/validar.py      (sale con código 1 si hay errores)
"""
import csv
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comun import EDITORIAL, HC, anclas, bloques, frontmatter, indice, leer, norm, paginas, titulo  # noqa: E402
import generar_faq  # noqa: E402

errores, avisos = [], []
PAGS = paginas()
TODOS = {**PAGS, **bloques()}

# 1. Menú
summary = leer(os.path.join(HC, "SUMMARY.md"))
en_menu = re.findall(r"\]\(([^)\s]+\.md)", summary)
for m in en_menu:
    if m not in PAGS:
        errores.append(f"Menú: la página {m} no existe")
for p in PAGS:
    if p not in en_menu:
        errores.append(f"Menú: {p} no está en el menú")
for p, t in PAGS.items():
    m = re.search(r"\[([^\]]+)\]\(" + re.escape(p) + r"(?:\s|\))", summary)
    if m and m.group(1).strip() != titulo(t):
        avisos.append(f"{p}: el título del menú no coincide con el H1")

# 2 y 3. Enlaces, anclas, imágenes, bloques, variables y estructura
vp = os.path.join(HC, ".gitbook", "vars.yaml")
vars_seccion = set(re.findall(r"^([A-Za-z]\w*):", leer(vp), flags=re.M)) if os.path.exists(vp) else set()
usados = set()
for p, t in TODOS.items():
    d = os.path.dirname(p)
    for tag in ["tabs", "tab", "stepper", "step", "hint", "content-ref"]:
        if len(re.findall(r"\{% " + tag + r"[ %]", t)) != len(re.findall(r"\{% end" + tag + r" %\}", t)):
            errores.append(f"{p}: bloque {tag} sin cerrar")
    if t.count("<details>") != t.count("</details>"):
        errores.append(f"{p}: bloque desplegable (details) sin cerrar")
    for ruta in re.findall(r'\{% include "([^"]+)" %\}', t):
        destino = norm(os.path.join(d, ruta))
        usados.add(destino)
        if destino not in TODOS:
            errores.append(f"{p}: bloque reutilizable inexistente {ruta}")
    for ruta, ancla in re.findall(r'(?:\]\(|(?:href|src|url)=")([^)"\s#]*)(?:#([^)"\s]+))?', t):
        if not ruta or re.match(r"^[a-z]+:", ruta):
            if not ruta and ancla and not p.startswith(".gitbook/") and ancla not in anclas(t)[1]:
                errores.append(f"{p}: ancla interna #{ancla} inexistente")
            continue
        destino = norm(os.path.join(d, ruta))
        if not os.path.exists(os.path.join(HC, destino)):
            errores.append(f"{p}: enlace o imagen rota {ruta}")
        elif ancla and destino in TODOS and ancla not in anclas(TODOS[destino])[1]:
            errores.append(f"{p}: ancla #{ancla} inexistente en {destino}")
    fm, _ = frontmatter(t)
    for v in re.findall(r"space\.vars\.(\w+)", t):
        if v not in vars_seccion:
            errores.append(f"{p}: variable de sección no definida {v}")
    for v in re.findall(r"page\.vars\.(\w+)", t):
        if v not in (fm.get("vars") or {}):
            errores.append(f"{p}: variable de página no definida {v}")
    if not p.startswith(".gitbook/") and not fm.get("description"):
        avisos.append(f"{p}: sin descripción (frontmatter description)")
for b in TODOS:
    if b.startswith(".gitbook/") and b not in usados:
        avisos.append(f"Bloque reutilizable sin usar: {b}")

# 4. Índice de contenidos
idx = indice()
en_indice = idx["paginas"]
for p in PAGS:
    if p not in en_indice:
        errores.append(f"Índice: falta la página {p}")
for p, datos in en_indice.items():
    if p not in PAGS:
        errores.append(f"Índice: la página {p} no existe")
        continue
    for t in datos.get("temas", []):
        if t not in idx["temas"]:
            errores.append(f"Índice: tema desconocido «{t}» en {p}")
    for r in datos.get("resuelve", []):
        if r["ancla"] and r["ancla"] not in anclas(PAGS[p])[0]:
            errores.append(f"Índice: el ancla fija #{r['ancla']} de {p} no existe")
    ft = datos.get("faq_tema")
    if ft:
        esperado = norm(os.path.relpath(f".gitbook/includes/faq-{ft}.md", os.path.dirname(p) or "."))
        if f'{{% include "{esperado}" %}}' not in PAGS[p]:
            errores.append(f"{p}: debe incluir el bloque de preguntas frecuentes faq-{ft}.md")
    elif datos["tipo"] == "tarea" and "includes/faq-" in PAGS[p]:
        errores.append(f"{p}: incluye preguntas frecuentes pero no tiene faq_tema en el índice")
    if datos["tipo"] in ("pregunta", "concepto") and not any(
            ft == t for d2 in en_indice.values() for ft in [d2.get("faq_tema")] for t in datos.get("temas", [])):
        avisos.append(f"{p}: ninguna tarea muestra esta pregunta (sus temas no son faq_tema de ninguna tarea)")

# 5. Bloques de preguntas frecuentes al día
for nombre, contenido in generar_faq.generar().items():
    ruta = os.path.join(HC, ".gitbook", "includes", nombre)
    if not os.path.exists(ruta) or leer(ruta) != contenido:
        errores.append(f"Bloque {nombre} desfasado: ejecuta herramientas/generar_faq.py")

# 6. Catálogo de enlaces contextuales
cat = os.path.join(EDITORIAL, "enlaces-contextuales.csv")
filas = 0
if os.path.exists(cat):
    with open(cat, encoding="utf-8-sig") as f:
        for fila in csv.DictReader(f, delimiter=";"):
            filas += 1
            pagina, ancla = fila["pagina"], fila.get("ancla", "")
            if pagina not in PAGS:
                errores.append(f"Catálogo {fila['id']}: la página {pagina} no existe")
            elif ancla and ancla not in anclas(PAGS[pagina])[0]:
                errores.append(f"Catálogo {fila['id']}: el ancla fija #{ancla} no existe en {pagina}")

RESUMEN = {
    "paginas": len(PAGS),
    "bloques": len([b for b in TODOS if b.startswith(".gitbook/")]),
    "variables": len(vars_seccion),
    "catalogo": filas,
    "errores": errores,
    "avisos": avisos,
}

if __name__ == "__main__":
    if "--json" in sys.argv:
        print(json.dumps(RESUMEN, ensure_ascii=False, indent=1))
        sys.exit(1 if errores else 0)
    print(f"Páginas: {len(PAGS)} · Bloques reutilizables: {RESUMEN['bloques']} · Variables: {len(vars_seccion)} · "
          f"Catálogo de enlaces: {filas}")
    for a in avisos:
        print("AVISO  ", a)
    for e in errores:
        print("ERROR  ", e)
    print("Resultado:", "correcto" if not errores else f"{len(errores)} errores")
    sys.exit(1 if errores else 0)
