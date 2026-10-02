"""Mantiene las preguntas frecuentes por tema a partir del índice editorial.

Lee _editorial/indice-contenido.yaml y mantiene al día:
  1. Los bloques reutilizables .gitbook/includes/faq-<tema>.md: uno por cada tema que muestra
     alguna tarea (faq_tema) o la portada de preguntas frecuentes y que tiene preguntas, con las
     páginas de tipo «pregunta» o «concepto» de ese tema, en el orden del menú. Un tema sin
     preguntas no tiene bloque.
  2. La parte «Preguntas frecuentes» del cierre «Más sobre…» de cada tarea: aparece solo si el
     tema de la tarea (faq_tema) tiene preguntas. Si no las tiene, se quita y, si el cierre se queda
     sin nada más, también su encabezado (criterio C1). Si el tema vuelve a tener preguntas, se
     añade de nuevo; cuando la tarea no tiene cierre, el encabezado se crea con «cierre» del índice.
     Una tarea sin faq_tema no muestra preguntas.
  3. La portada de preguntas frecuentes (preguntas-frecuentes/README.md), con las secciones de
     «portada_faq» del índice: cada sección muestra los bloques de sus temas que tienen preguntas
     y no aparece si no tiene ninguna.

Para que una pregunta aparezca en las tareas de un tema y en la portada basta con añadir el tema
a su entrada del índice y volver a ejecutar este script. La parte «Preguntas frecuentes» del cierre
y la portada no se editan a mano; el resto del cierre («También te puede interesar») sí.

Uso:
  python herramientas/generar_faq.py             escribe bloques, cierres y portada
  python herramientas/generar_faq.py --comprobar  solo comprueba que están al día (sale con 1 si no)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comun import HC, INCLUDES, indice, leer, norm, escribir, titulo  # noqa: E402

TIPOS_FAQ = {"pregunta", "concepto"}
PORTADA = "preguntas-frecuentes/README.md"
RE_CIERRE = re.compile(r"^## Más sobre .*$", re.M)
RE_PARTE = re.compile(r'\*\*Preguntas frecuentes\*\*\n\n\{% include "[^"]*faq-[\w-]+\.md" %\}\n\n?')


def orden_menu():
    summary = leer(os.path.join(HC, "SUMMARY.md"))
    return re.findall(r"\]\(([^)\s]+\.md)", summary)


def preguntas_por_tema(idx):
    orden = orden_menu()
    res = {}
    for tema in idx["temas"]:
        preguntas = [ruta for ruta, p in idx["paginas"].items()
                     if p["tipo"] in TIPOS_FAQ and tema in p.get("temas", [])]
        preguntas.sort(key=lambda r: orden.index(r) if r in orden else 999)
        res[tema] = preguntas
    return res


def temas_mostrados(idx):
    temas = {p["faq_tema"] for p in idx["paginas"].values() if p.get("faq_tema")}
    for seccion in idx.get("portada_faq", []):
        temas.update(seccion["temas"])
    return temas


def temas_con_preguntas(idx):
    pq = preguntas_por_tema(idx)
    return {t for t in temas_mostrados(idx) if pq.get(t)}


def generar():
    """{nombre de archivo: contenido} de los bloques de preguntas frecuentes."""
    idx = indice()
    pq = preguntas_por_tema(idx)
    salida = {}
    for tema in sorted(temas_con_preguntas(idx)):
        lineas = ["---", f"title: Preguntas frecuentes – {idx['temas'][tema]}", "---", ""]
        for ruta in pq[tema]:
            texto = leer(os.path.join(HC, ruta))
            enlace = norm(os.path.relpath(ruta, ".gitbook/includes"))
            lineas.append(f"* [{titulo(texto)}]({enlace})")
        lineas.append("")
        salida[f"faq-{tema}.md"] = "\n".join(lineas)
    return salida


def sobrantes(generados):
    """Bloques faq-*.md que existen pero ya no corresponden a ningún tema con preguntas."""
    return sorted(a for a in os.listdir(INCLUDES)
                  if a.startswith("faq-") and a.endswith(".md") and a not in generados)


def include(ruta_pagina, tema):
    destino = norm(os.path.relpath(f".gitbook/includes/faq-{tema}.md", os.path.dirname(ruta_pagina) or "."))
    return f'{{% include "{destino}" %}}'


def cierre_tarea(ruta, datos, texto, con_preguntas):
    """Texto de la tarea con la parte «Preguntas frecuentes» del cierre al día, o None si falta «cierre»."""
    tema = datos.get("faq_tema")
    mostrar = bool(tema) and tema in con_preguntas
    parte = f"**Preguntas frecuentes**\n\n{include(ruta, tema)}\n\n" if mostrar else ""
    m = RE_CIERRE.search(texto)
    if m:
        cuerpo = texto[:m.start()]
        cabecera, _, resto = texto[m.start():].partition("\n")
        resto = RE_PARTE.sub("", resto.lstrip("\n"), count=1)
        nuevo = (parte + resto).rstrip("\n")
        if not nuevo:
            return cuerpo.rstrip("\n") + "\n"
        return cuerpo + cabecera + "\n\n" + nuevo + "\n"
    if not mostrar:
        return texto
    cierre = datos.get("cierre")
    if not cierre:
        return None
    ancla = cierre["ancla"]
    return (texto.rstrip("\n") + f'\n\n## {cierre["titulo"]} <a href="#{ancla}" id="{ancla}"></a>\n\n'
            + parte.rstrip("\n") + "\n")


def portada(idx, con_preguntas):
    texto = leer(os.path.join(HC, PORTADA))
    i = texto.find("\n## ")
    cabecera = texto[:i + 1] if i >= 0 else texto.rstrip("\n") + "\n\n"
    secciones = []
    for s in idx.get("portada_faq", []):
        temas = [t for t in s["temas"] if t in con_preguntas]
        if not temas:
            continue
        bloques = "\n\n".join(include(PORTADA, t) for t in temas)
        secciones.append(f'## {s["titulo"]} <a href="#{s["ancla"]}" id="{s["ancla"]}"></a>\n\n{bloques}\n')
    return cabecera + "\n".join(secciones)


def paginas_al_dia():
    """({ruta: contenido esperado} de las tareas y la portada, [errores])."""
    idx = indice()
    con = temas_con_preguntas(idx)
    res, errores = {}, []
    for ruta, datos in idx["paginas"].items():
        if datos["tipo"] != "tarea":
            continue
        nuevo = cierre_tarea(ruta, datos, leer(os.path.join(HC, ruta)), con)
        if nuevo is None:
            errores.append(f"{ruta}: su tema tiene preguntas y no tiene cierre; añade «cierre» (titulo, ancla) en el índice")
            continue
        res[ruta] = nuevo
    if idx.get("portada_faq"):
        res[PORTADA] = portada(idx, con)
    return res, errores


def main():
    comprobar = "--comprobar" in sys.argv
    desfasados = []
    bloques_gen = generar()
    cambios = {os.path.join(INCLUDES, n): (f".gitbook/includes/{n}", c) for n, c in bloques_gen.items()}
    paginas, errores = paginas_al_dia()
    cambios.update({os.path.join(HC, r): (r, c) for r, c in paginas.items()})
    for ruta, (nombre, contenido) in cambios.items():
        actual = leer(ruta) if os.path.exists(ruta) else None
        if actual == contenido:
            continue
        desfasados.append(nombre)
        if comprobar:
            print(f"DESFASADO  {nombre}")
        else:
            escribir(ruta, contenido)
            print(f"{'creado' if actual is None else 'actualizado':<12}{nombre}")
    for a in sobrantes(bloques_gen):
        desfasados.append(a)
        print(f"SOBRANTE    .gitbook/includes/{a}: ya no se usa; bórralo (git rm)")
    for e in errores:
        print(f"ERROR       {e}")
    if not desfasados and not errores:
        print(f"al día      {len(bloques_gen)} bloques, {len(paginas)} páginas")
    if (comprobar and desfasados) or errores:
        if comprobar:
            print("Ejecuta: python herramientas/generar_faq.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
