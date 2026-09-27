"""Aplica los enlaces por intención de _editorial/enlaces-propuestos.json.

Cada propuesta indica la frase exacta de la página («buscar»), qué parte se enlaza («texto»,
por defecto toda la frase) y el destino (ruta relativa a la página, con ancla opcional, o
«externo:<clave>» del índice de contenidos). Las propuestas de tipo «añadir» insertan una frase
nueva con el enlace («insertar_antes» o «insertar_despues» de «buscar»).

Solo se aplican las propuestas con estado «aceptado». Una vez aplicadas pasan a «aplicado».
Las rechazadas se quedan en el archivo como «rechazado» para no volver a proponerlas.

Uso:
  python herramientas/aplicar_enlaces.py              aplica las aceptadas
  python herramientas/aplicar_enlaces.py --comprobar  solo comprueba que todas se pueden aplicar
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comun import EDITORIAL, HC, escribir, indice, leer  # noqa: E402

ARCHIVO = os.path.join(EDITORIAL, "enlaces-propuestos.json")


def cargar():
    return json.loads(leer(ARCHIVO))


def guardar(propuestas):
    lineas = ",\n".join("  " + json.dumps(p, ensure_ascii=False) for p in propuestas)
    escribir(ARCHIVO, "[\n" + lineas + "\n]\n")


def url_destino(destino, externos):
    if destino.startswith("externo:"):
        return externos[destino.split(":", 1)[1]]["url"]
    return destino


def dentro_de_enlace(texto, pos):
    """True si la posición está dentro del texto de un enlace markdown o de una etiqueta HTML."""
    inicio_linea = texto.rfind("\n", 0, pos) + 1
    antes = texto[inicio_linea:pos]
    if antes.count("[") > antes.count("]"):
        return True
    if antes.count("<") > antes.count(">"):
        return True
    return False


def localizar(texto, frase):
    """Posiciones donde aparece la frase fuera de enlaces, títulos y bloques de código."""
    res = []
    for m in re.finditer(re.escape(frase), texto):
        linea = texto[texto.rfind("\n", 0, m.start()) + 1:]
        if linea.startswith("#") or linea.startswith("```") or dentro_de_enlace(texto, m.start()):
            continue
        res.append(m.start())
    return res


def aplicar(texto, p, externos, marcar=False):
    """Devuelve (texto nuevo, problema o None). Con marcar=True añade un título para la vista previa."""
    frase = p["buscar"]
    pos = localizar(texto, frase)
    if not pos:
        return texto, "no se encuentra la frase (o ya está enlazada)"
    if len(pos) > 1:
        return texto, f"la frase aparece {len(pos)} veces; hay que ampliarla"
    i = pos[0]
    url = url_destino(p["destino"], externos)
    titulo = f' "PROPUESTO {p["id"]}"' if marcar else ""
    if p["tipo"] == "enlazar":
        parte = p.get("texto", frase)
        j = frase.find(parte)
        if j == -1:
            return texto, "«texto» no está dentro de «buscar»"
        k = i + j
        return texto[:k] + f"[{parte}]({url}{titulo})" + texto[k + len(parte):], None
    if p["tipo"] == "añadir":
        nuevo = p.get("insertar_antes") or p.get("insertar_despues")
        nuevo = re.sub(r"\]\(([^)\s]+)\)", lambda m: f"]({url_destino(m.group(1), externos)}{titulo})", nuevo)
        if p.get("insertar_antes"):
            return texto[:i] + nuevo + texto[i:], None
        k = i + len(frase)
        return texto[:k] + nuevo + texto[k:], None
    return texto, f"tipo desconocido {p['tipo']}"


def main():
    comprobar = "--comprobar" in sys.argv
    externos = indice().get("externos", {})
    propuestas = cargar()
    textos, problemas, aplicadas = {}, 0, 0
    for p in propuestas:
        if p["estado"] in ("aplicado", "rechazado"):
            continue
        ruta = os.path.join(HC, p["pagina"])
        if p["pagina"] not in textos:
            textos[p["pagina"]] = leer(ruta)
        nuevo, problema = aplicar(textos[p["pagina"]], p, externos)
        if problema:
            problemas += 1
            print(f"PROBLEMA  {p['id']} {p['pagina']}: {problema}")
            continue
        if p["estado"] == "aceptado" and not comprobar:
            textos[p["pagina"]] = nuevo
            p["estado"] = "aplicado"
            aplicadas += 1
            print(f"aplicado  {p['id']} {p['pagina']}")
    if not comprobar and aplicadas:
        for pagina, texto in textos.items():
            escribir(os.path.join(HC, pagina), texto)
        guardar(propuestas)
    pendientes = sum(1 for p in propuestas if p["estado"] in ("propuesto", "aceptado"))
    print(f"Aplicadas ahora: {aplicadas} · Pendientes de decisión: {pendientes} · Problemas: {problemas}")
    sys.exit(1 if problemas else 0)


if __name__ == "__main__":
    main()
