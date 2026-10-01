"""Genera la lista única de pendientes del borrador: _editorial/pendientes.md.

Fuentes:
  - _editorial/pendientes.yaml: una entrada por pendiente, sobre una página, un bloque reutilizable o
    una variable. Está fuera de help-center, así que GitBook no la importa ni la reescribe: los
    pendientes no se pierden si una página se edita en GitBook.
  - Las imágenes con texto alternativo «Imagen de la app que falta: …» (tipo «captura de la app»).

No se usan comentarios en las páginas ni en vars.yaml: GitBook los elimina al devolver a GitHub una
página editada en su editor, y reescribe vars.yaml sin comentarios en cada fusión (prueba del 01/10/2026).

Cada entrada de pendientes.yaml:
  - pagina: ruta en help-center | bloque: nombre del bloque | variable: nombre de la variable
    cita: fragmento literal del texto afectado (opcional en bloques y variables); localiza la línea y la
          sección. Si el texto cambia, validar.py avisa para revisar el pendiente.
    tipo: uno de TIPOS (contradicción con el número del análisis, 1 a 11)
    texto: qué falta o qué hay que validar, con su referencia (Pnn)

Los pendientes de un bloque o de una variable se listan una vez con todas las páginas que los usan
y también en cada una de esas páginas.

Uso:
  python herramientas/generar_pendientes.py              escribe _editorial/pendientes.md
  python herramientas/generar_pendientes.py --comprobar  solo comprueba (sale con 1 si está desfasada)
"""
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from comun import EDITORIAL, HC, bloques, escribir, leer, norm, paginas, slug, titulo  # noqa: E402

GITBOOK = "https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/"
FUENTE = os.path.join(EDITORIAL, "pendientes.yaml")
SALIDA = os.path.join(EDITORIAL, "pendientes.md")

TIPOS = {
    "contradicción": "incoherencia de negocio del análisis de contenido, apartado 4 (con su número)",
    "valor provisional": "dato que figura en la ayuda pero falta confirmar",
    "app": "funcionamiento o texto de la app sin confirmar",
    "captura de la app": "falta la captura de la app (marcador de imagen)",
    "captura dudosa": "captura usada que conviene revisar",
    "captura descartada": "captura original no usada, con el motivo",
    "sin verificar": "contenido funcional sin fuente o genérico",
    "decisión": "decisión editorial o de estructura pendiente de Sergio",
}
ORDEN_TIPOS = list(TIPOS)
RE_APP = re.compile(r'alt="Imagen de la app que falta:\s*([^"]*)"')
RE_H2 = re.compile(r"^## (.+?)\s*$", re.M)


def base_tipo(tipo):
    return "contradicción" if tipo.startswith("contradicción") else tipo


def tipo_valido(tipo):
    t = str(tipo).strip()
    if t.startswith("contradicción"):
        n = t[len("contradicción"):].strip()
        return n.isdigit() and 1 <= int(n) <= 11
    return t in TIPOS


def fuente():
    if not os.path.exists(FUENTE):
        return []
    return yaml.safe_load(leer(FUENTE)) or []


def grupos_menu():
    """{ruta: slug del grupo de SUMMARY.md}. En GitBook la URL es grupo/página, no la carpeta."""
    res, grupo = {}, ""
    for linea in leer(os.path.join(HC, "SUMMARY.md")).splitlines():
        if linea.startswith("## "):
            grupo = slug(linea[3:])
        m = re.match(r"\s*\* \[[^\]]*\]\(([^)\s]+\.md)", linea)
        if m:
            res[m.group(1)] = grupo
    return res


def url_pagina(ruta):
    if ruta == "README.md":
        return GITBOOK
    if ruta.endswith("/README.md"):
        return GITBOOK + ruta[: -len("/README.md")]
    grupos = grupos_menu()
    if ruta not in grupos:
        return GITBOOK + ruta[:-3]
    grupo = grupos[ruta]
    return GITBOOK + (grupo + "/" if grupo else "") + os.path.basename(ruta)[:-3]


def seccion(ruta, texto, pos):
    """Enlace Markdown a la sección (último ## antes de pos) o «Inicio de la página»."""
    tit, ancla = None, None
    for m in RE_H2.finditer(texto[:pos]):
        cab = m.group(1)
        fija = re.search(r'id="([^"]+)"', cab)
        tit = re.sub(r"<[^>]+>", "", cab).strip()
        ancla = fija.group(1) if fija else slug(cab)
    return f"[{tit}]({url_pagina(ruta)}#{ancla})" if tit else "Inicio de la página"


def linea(texto, pos):
    return texto.count("\n", 0, pos) + 1


def celda(t):
    return " ".join(str(t).split()).replace("|", "\\|")


def ruta_bloque(nombre):
    return f".gitbook/includes/{nombre}.md"


def usos():
    """({bloque: [(página, pos)]}, {variable: [(página, pos)]}) incluidas las variables dentro de bloques."""
    pags, blqs = paginas(), bloques()
    ub, uv = {}, {}
    for p, t in pags.items():
        for m in re.finditer(r'\{% include "([^"]+)" %\}', t):
            destino = norm(os.path.join(os.path.dirname(p), m.group(1)))
            ub.setdefault(destino, []).append((p, m.start()))
            for v in set(re.findall(r"space\.vars\.(\w+)", blqs.get(destino, ""))):
                uv.setdefault(v, []).append((p, m.start()))
        for m in re.finditer(r"space\.vars\.(\w+)", t):
            uv.setdefault(m.group(1), []).append((p, m.start()))
    return ub, uv


def errores():
    """Entradas de pendientes.yaml incorrectas o que ya no localizan su texto, y comentarios PENDIENTE sueltos."""
    pags, blqs = paginas(), bloques()
    vp = os.path.join(HC, ".gitbook", "vars.yaml")
    vars_ = set(re.findall(r"^([A-Za-z]\w*):", leer(vp), flags=re.M)) if os.path.exists(vp) else set()
    errs = []
    for i, e in enumerate(fuente(), 1):
        donde = f"_editorial/pendientes.yaml, entrada {i}"
        if not isinstance(e, dict):
            errs.append(f"{donde}: formato incorrecto")
            continue
        claves = [k for k in ("pagina", "bloque", "variable") if e.get(k)]
        if len(claves) != 1:
            errs.append(f"{donde}: indica una sola de pagina, bloque o variable")
            continue
        if not tipo_valido(e.get("tipo", "")):
            errs.append(f"{donde}: tipo desconocido «{e.get('tipo')}»")
        if not str(e.get("texto", "")).strip():
            errs.append(f"{donde}: falta el texto")
        cita = e.get("cita")
        if e.get("pagina"):
            p = e["pagina"]
            if p not in pags:
                errs.append(f"{donde}: la página {p} no existe")
            elif not cita:
                errs.append(f"{donde}: falta la cita que localiza el pendiente en {p}")
            elif cita not in pags[p]:
                errs.append(f"{donde}: la cita «{cita}» ya no está en {p}; revisa el pendiente")
        elif e.get("bloque"):
            b = ruta_bloque(e["bloque"])
            if b not in blqs:
                errs.append(f"{donde}: el bloque {e['bloque']} no existe")
            elif cita and cita not in blqs[b]:
                errs.append(f"{donde}: la cita «{cita}» ya no está en el bloque {e['bloque']}; revisa el pendiente")
        elif e["variable"] not in vars_:
            errs.append(f"{donde}: la variable {e['variable']} no existe en vars.yaml")
    for ruta, texto in {**pags, **blqs}.items():
        if "<!-- PENDIENTE" in texto:
            errs.append(f"{ruta}: comentario PENDIENTE en el contenido; los pendientes van en _editorial/pendientes.yaml")
    return errs


def generar():
    pags, blqs = paginas(), bloques()
    ub, uv = usos()
    menu = re.findall(r"\]\(([^)\s]+\.md)", leer(os.path.join(HC, "SUMMARY.md")))
    por_pagina, compartidos, cuenta = {}, {}, {}

    def anota(p, pos, tipo, txt, enl):
        por_pagina.setdefault(p, []).append((pos, seccion(p, pags[p], pos), tipo, txt, enl))

    entradas = list(fuente())
    for p, t in pags.items():
        for m in RE_APP.finditer(t):
            entradas.append({"pagina": p, "tipo": "captura de la app", "texto": m.group(1).strip(), "_pos": m.start()})
    for e in entradas:
        if not isinstance(e, dict) or not tipo_valido(e.get("tipo", "")):
            continue
        tipo, txt = str(e["tipo"]).strip(), celda(e.get("texto", ""))
        cuenta[base_tipo(tipo)] = cuenta.get(base_tipo(tipo), 0) + 1
        cita = e.get("cita")
        if e.get("pagina") in pags:
            p, t = e["pagina"], pags[e["pagina"]]
            pos = e.get("_pos", t.find(cita) if cita and cita in t else 0)
            anota(p, pos, tipo, txt, f"[L{linea(t, pos)}](../help-center/{p}#L{linea(t, pos)})")
        elif e.get("bloque") and ruta_bloque(e["bloque"]) in blqs:
            b = ruta_bloque(e["bloque"])
            t = blqs[b]
            pos = t.find(cita) if cita and cita in t else 0
            enl = f"[L{linea(t, pos)}](../help-center/{b}#L{linea(t, pos)})"
            compartidos.setdefault(f"Bloque `{e['bloque']}`", ([], ub.get(b, [])))[0].append((tipo, txt, enl))
            for p, pos2 in ub.get(b, []):
                anota(p, pos2, tipo, f"Bloque `{e['bloque']}`: {txt}", enl)
        elif e.get("variable"):
            v = e["variable"]
            vp = leer(os.path.join(HC, ".gitbook", "vars.yaml"))
            m = re.search(r"^" + re.escape(v) + r":", vp, flags=re.M)
            n = linea(vp, m.start()) if m else 1
            enl = f"[L{n}](../help-center/.gitbook/vars.yaml#L{n})"
            compartidos.setdefault(f"Variable `{v}`", ([], uv.get(v, [])))[0].append((tipo, txt, enl))
            for p, pos2 in uv.get(v, []):
                anota(p, pos2, tipo, f"Variable `{v}`: {txt}", enl)

    n_comp = sum(len(c[0]) for c in compartidos.values())
    n_total = sum(cuenta.values())
    out = ["# Pendientes del borrador", "",
           "Lista generada por `herramientas/generar_pendientes.py` a partir de `_editorial/pendientes.yaml` y de los "
           "marcadores de captura de la app. No se edita a mano: se corrige la fuente y se vuelve a generar. "
           "GitBook no importa esta carpeta.", "",
           f"**{n_total} pendientes**: {n_total - n_comp} en páginas y {n_comp} en bloques o variables compartidos, "
           f"que se repiten en cada página donde se usan. {len(por_pagina)} páginas afectadas.", "",
           "| Tipo | Qué significa | Número |", "|---|---|---|"]
    for t in ORDEN_TIPOS:
        out.append(f"| {t} | {TIPOS[t]} | {cuenta.get(t, 0)} |")
    out += ["", "## Bloques y variables compartidos", ""]
    if not compartidos:
        out += ["Ninguno.", ""]
    for nombre in sorted(compartidos):
        lista, us = compartidos[nombre]
        out += [f"### {nombre}", "", "| Tipo | Pendiente | Línea |", "|---|---|---|"]
        for tipo, txt, enl in lista:
            out.append(f"| {tipo} | {txt} | {enl} |")
        afect = []
        for p, pos in us:
            s = seccion(p, pags[p], pos)
            d = f"[{titulo(pags[p]) or p}]({url_pagina(p)})" + (f" › {s}" if s != "Inicio de la página" else "")
            if d not in afect:
                afect.append(d)
        out += ["", "Páginas afectadas: " + ("; ".join(afect) if afect else "ninguna") + ".", ""]
    out += ["## Por página", ""]
    orden = [p for p in menu if p in por_pagina] + sorted(p for p in por_pagina if p not in menu)
    if not orden:
        out += ["Ninguna.", ""]
    for p in orden:
        out += [f"### [{titulo(pags[p]) or p}]({url_pagina(p)})", "", f"`{p}`", "",
                "| Sección | Tipo | Pendiente | Línea |", "|---|---|---|---|"]
        for _, sec, tipo, txt, enl in sorted(por_pagina[p], key=lambda x: x[0]):
            out.append(f"| {sec} | {tipo} | {txt} | {enl} |")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def main():
    errs = errores()
    for e in errs:
        print("ERROR  ", e)
    contenido = generar()
    actual = leer(SALIDA) if os.path.exists(SALIDA) else None
    if "--comprobar" in sys.argv:
        print("al día     _editorial/pendientes.md" if actual == contenido
              else "DESFASADO  _editorial/pendientes.md · ejecuta: python herramientas/generar_pendientes.py")
        sys.exit(1 if errs or actual != contenido else 0)
    if actual != contenido:
        escribir(SALIDA, contenido)
        print(f"{'creado' if actual is None else 'actualizado':<10} _editorial/pendientes.md")
    else:
        print("al día     _editorial/pendientes.md")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
