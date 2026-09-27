"""Genera los bloques reutilizables de preguntas frecuentes por tema.

Lee _editorial/indice-contenido.yaml y, por cada tema que alguna tarea muestra (faq_tema),
escribe help-center/.gitbook/includes/faq-<tema>.md con las páginas de tipo «pregunta» o
«concepto» etiquetadas con ese tema, en el orden del menú.

Para que una pregunta aparezca en las tareas de un tema basta con añadir el tema a su
entrada del índice y volver a ejecutar este script. No se editan las tareas.

Uso:
  python herramientas/generar_faq.py             escribe los bloques
  python herramientas/generar_faq.py --comprobar  solo comprueba que están al día (sale con 1 si no)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comun import HC, INCLUDES, indice, leer, norm, escribir, titulo  # noqa: E402

TIPOS_FAQ = {"pregunta", "concepto"}


def orden_menu():
    summary = leer(os.path.join(HC, "SUMMARY.md"))
    return re.findall(r"\]\(([^)\s]+\.md)", summary)


def generar():
    """{nombre de archivo: contenido} de los bloques de preguntas frecuentes."""
    idx = indice()
    orden = orden_menu()
    temas_usados = sorted({p["faq_tema"] for p in idx["paginas"].values() if p.get("faq_tema")})
    salida = {}
    for tema in temas_usados:
        preguntas = [ruta for ruta, p in idx["paginas"].items()
                     if p["tipo"] in TIPOS_FAQ and tema in p.get("temas", [])]
        preguntas.sort(key=lambda r: orden.index(r) if r in orden else 999)
        nombre_tema = idx["temas"][tema]
        lineas = ["---", f"title: Preguntas frecuentes – {nombre_tema}", "---", ""]
        for ruta in preguntas:
            texto = leer(os.path.join(HC, ruta))
            enlace = norm(os.path.relpath(ruta, ".gitbook/includes"))
            lineas.append(f"* [{titulo(texto)}]({enlace})")
        lineas.append("")
        salida[f"faq-{tema}.md"] = "\n".join(lineas)
    return salida


def main():
    comprobar = "--comprobar" in sys.argv
    desfasados = []
    for nombre, contenido in generar().items():
        ruta = os.path.join(INCLUDES, nombre)
        actual = leer(ruta) if os.path.exists(ruta) else None
        if actual == contenido:
            print(f"al día     .gitbook/includes/{nombre}")
            continue
        desfasados.append(nombre)
        if comprobar:
            print(f"DESFASADO  .gitbook/includes/{nombre}")
        else:
            escribir(ruta, contenido)
            print(f"{'creado' if actual is None else 'actualizado':<10} .gitbook/includes/{nombre}")
    if comprobar and desfasados:
        print("Ejecuta: python herramientas/generar_faq.py")
        sys.exit(1)


if __name__ == "__main__":
    main()
