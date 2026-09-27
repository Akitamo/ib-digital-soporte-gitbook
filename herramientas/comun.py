"""Funciones comunes de las herramientas del centro de ayuda (sección Personas)."""
import os
import re
import unicodedata

import yaml

REPO = os.path.abspath(os.environ.get("REPO_GITBOOK", os.path.join(os.path.dirname(__file__), "..")))
HC = os.path.join(REPO, "help-center")
EDITORIAL = os.path.join(REPO, "_editorial")
INCLUDES = os.path.join(HC, ".gitbook", "includes")


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def norm(ruta):
    return os.path.normpath(ruta).replace(os.sep, "/")


def rel(desde_pagina, hasta_pagina):
    """Ruta relativa entre dos páginas de help-center (ambas relativas a help-center)."""
    return norm(os.path.relpath(hasta_pagina, os.path.dirname(desde_pagina) or "."))


def indice():
    return yaml.safe_load(leer(os.path.join(EDITORIAL, "indice-contenido.yaml")))


def frontmatter(texto):
    """Devuelve (dict, cuerpo)."""
    if texto.startswith("---\n"):
        fin = texto.find("\n---", 4)
        if fin != -1:
            return yaml.safe_load(texto[4:fin]) or {}, texto[fin + 4:].lstrip("\n")
    return {}, texto


def titulo(texto):
    m = re.search(r"^# (.+)$", texto, flags=re.M)
    return m.group(1).strip() if m else ""


def slug(texto):
    texto = re.sub(r"<[^>]+>", "", texto)
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    texto = re.sub(r"[^\w\s-]", "", texto.lower()).strip()
    return re.sub(r"[\s_]+", "-", texto)


def anclas(texto):
    """(anclas fijas, todas las anclas) de una página."""
    fijas = set(re.findall(r'id="([^"]+)"', texto))
    auto = {slug(h) for h in re.findall(r"^#{1,6} (.+)$", texto, flags=re.M)}
    return fijas, fijas | auto


def paginas():
    """{ruta relativa a help-center: texto} de todas las páginas (sin SUMMARY ni bloques)."""
    res = {}
    for raiz, _, archivos in os.walk(HC):
        if "/.gitbook" in norm(raiz) + "/":
            continue
        for a in sorted(archivos):
            if a.endswith(".md") and a != "SUMMARY.md":
                res[norm(os.path.relpath(os.path.join(raiz, a), HC))] = leer(os.path.join(raiz, a))
    return res


def bloques():
    """{'.gitbook/includes/x.md': texto}"""
    res = {}
    if os.path.isdir(INCLUDES):
        for a in sorted(os.listdir(INCLUDES)):
            if a.endswith(".md"):
                res[f".gitbook/includes/{a}"] = leer(os.path.join(INCLUDES, a))
    return res
