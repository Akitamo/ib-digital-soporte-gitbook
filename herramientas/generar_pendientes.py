"""Genera la lista única de pendientes del borrador: _editorial/pendientes.md.

Recoge tres tipos de marcador:
  - en páginas y bloques reutilizables, un comentario en su propia línea, justo antes de lo afectado:
        <!-- PENDIENTE [tipo]: qué falta o qué hay que validar (referencia) -->
  - en .gitbook/vars.yaml, un comentario en la línea anterior a la variable:
        # PENDIENTE [valor provisional]: …
  - imágenes con texto alternativo «Imagen de la app que falta: …» (tipo «captura de la app»).

Los pendientes de un bloque o de una variable se listan una vez, con todas las páginas que los usan,
y también en cada una de esas páginas. Cada fila enlaza a la página y sección en GitBook y a la línea
del archivo en GitHub.

La lista no se edita a mano: se corrige el marcador y se vuelve a generar. validar.py comprueba que
los marcadores son correctos y que la lista está al día.

Uso:
  python herramientas/generar_pendientes.py              escribe _editorial/pendientes.md
  python herramientas/generar_pendientes.py --comprobar  solo comprueba (sale con 1 si está desfasada)
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from comun import EDITORIAL, HC, bloques, escribir, leer, norm, paginas, slug, titulo  # noqa: E402

GITBOOK = "https://app.gitbook.com/o/R2iiSe67DRkUjor1gjhY/s/Z5e2C4G5OriqT5L8gO9x/"
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

RE_MARCA = re.compile(r"<!--\s*PENDIENTE\s*\[([^\]]+)\]\s*:\s*(.*?)\s*-->", re.S)
RE_MARCA_SUELTA = re.compile(r"<!--\s*PENDIENTE(?!\s*\[[^\]]+\]\s*:)", re.S)
RE_APP = re.compile(r'alt="Imagen de la app que falta:\s*([^"]*)"')
RE_VAR_MARCA = re.compile(r"^#\s*PENDIENTE\s*\[([^\]]+)\]\s*:\s*(.*)$")
RE_H2 = re.compile(r"^## (.+?)\s*$")


def tipo_valido(tipo):
    t = tipo.strip()
    if t.startswith("contradicción"):
        n = t[len("contradicción"):].strip()
        return n.isdigit() and 1 <= int(n) <= 11
    return t in TIPOS


def clave_tipo(tipo):
    base = "contradicción" if tipo.startswith("contradicción") else tipo
    n = int(tipo.split()[-1]) if base == "contradicción" else 0
    return (ORDEN_TIPOS.index(base) if base in ORDEN_TIPOS else 99, n)


def url_pagina(ruta):
    if ruta == "README.md":
        return GITBOOK
    if ruta.endswith("/README.md"):
        return GITBOOK + ruta[: -len("/README.md")]
    return GITBOOK + ruta[:-3]


def seccion_en(texto, pos):
    """(título, ancla) del último encabezado ## antes de pos; (None, None) si no hay."""
    tit, ancla = None, None
    for n, linea in enumerate(texto[:pos].split("\n")):
        m = RE_H2.match(linea)
        if m:
            cab = m.group(1)
            fija = re.search(r'id="([^"]+)"', cab)
            tit = re.sub(r"<[^>]+>", "", cab).strip()
            ancla = fija.group(1) if fija else slug(cab)
    return tit, ancla


def linea_de(texto, pos):
    return texto.count("\n", 0, pos) + 1


def marcas(texto):
    """[(pos, tipo, texto)] de un archivo Markdown."""
    res = [(m.start(), m.group(1).strip(), " ".join(m.group(2).split())) for m in RE_MARCA.finditer(texto)]
    res += [(m.start(), "captura de la app", m.group(1).strip()) for m in RE_APP.finditer(texto)]
    return sorted(res)


def marcas_vars():
    """{variable: [(línea, tipo, texto)]} de .gitbook/vars.yaml."""
    ruta = os.path.join(HC, ".gitbook", "vars.yaml")
    res = {}
    if not os.path.exists(ruta):
        return res
    pend = []
    for n, linea in enumerate(leer(ruta).split("\n"), 1):
        m = RE_VAR_MARCA.match(linea.strip())
        if m:
            pend.append((n, m.group(1).strip(), m.group(2).strip()))
            continue
        v = re.match(r"^([A-Za-z]\w*):", linea)
        if v:
            if pend:
                res[v.group(1)] = pend
            pend = []
    return res


def errores_marcas():
    """Marcadores mal formados o con tipo desconocido."""
    errs = []
    for ruta, texto in {**paginas(), **bloques()}.items():
        for m in RE_MARCA_SUELTA.finditer(texto):
            errs.append(f"{ruta}:{linea_de(texto, m.start())}: marcador PENDIENTE sin el formato <!-- PENDIENTE [tipo]: texto -->")
        for m in RE_MARCA.finditer(texto):
            if not tipo_valido(m.group(1)):
                errs.append(f"{ruta}:{linea_de(texto, m.start())}: tipo de pendiente desconocido «{m.group(1).strip()}»")
            if not m.group(2).strip():
                errs.append(f"{ruta}:{linea_de(texto, m.start())}: pendiente sin descripción")
    for var, lista in marcas_vars().items():
        for n, tipo, txt in lista:
            if not tipo_valido(tipo) or not txt:
                errs.append(f".gitbook/vars.yaml:{n}: pendiente de la variable {var} mal formado")
    return errs


def orden_menu():
    return re.findall(r"\]\(([^)\s]+\.md)", leer(os.path.join(HC, "SUMMARY.md")))


def enlace_archivo(ruta, linea):
    return f"[L{linea}](../help-center/{ruta}#L{linea})"


def celda(t):
    return t.replace("|", "\\|")


def generar():
    pags, blqs = paginas(), bloques()
    vmarcas = marcas_vars()
    menu = orden_menu()

    # Usos de bloques y variables: {nombre: [(página, pos)]}
    usos_bloque, usos_var = {}, {}
    for p, t in pags.items():
        for m in re.finditer(r'\{% include "([^"]+)" %\}', t):
            destino = norm(os.path.join(os.path.dirname(p), m.group(1)))
            usos_bloque.setdefault(destino, []).append((p, m.start()))
            for v in re.findall(r"space\.vars\.(\w+)", blqs.get(destino, "")):
                usos_var.setdefault(v, []).append((p, m.start()))
        for m in re.finditer(r"space\.vars\.(\w+)", t):
            usos_var.setdefault(m.group(1), []).append((p, m.start()))

    def destino_txt(p, pos):
        tit, ancla = seccion_en(pags[p], pos)
        nombre = titulo(pags[p]) or p
        if tit:
            return f"[{nombre}]({url_pagina(p)}) › [{tit}]({url_pagina(p)}#{ancla})"
        return f"[{nombre}]({url_pagina(p)})"

    por_pagina, compartidos = {}, []
    for p, t in pags.items():
        for pos, tipo, txt in marcas(t):
            tit, ancla = seccion_en(t, pos)
            sec = f"[{tit}]({url_pagina(p)}#{ancla})" if tit else "Inicio de la página"
            por_pagina.setdefault(p, []).append((pos, sec, tipo, txt, enlace_archivo(p, linea_de(t, pos))))
    for b, t in blqs.items():
        lista = marcas(t)
        if not lista:
            continue
        nombre = os.path.basename(b)[:-3]
        usos = usos_bloque.get(b, [])
        compartidos.append((f"Bloque `{nombre}`", [(tipo, txt, enlace_archivo(b, linea_de(t, pos))) for pos, tipo, txt in lista], usos))
        for p, pos in usos:
            tit, ancla = seccion_en(pags[p], pos)
            sec = f"[{tit}]({url_pagina(p)}#{ancla})" if tit else "Inicio de la página"
            for pos2, tipo, txt in lista:
                por_pagina.setdefault(p, []).append((pos, sec, tipo, f"Bloque `{nombre}`: {txt}", enlace_archivo(b, linea_de(t, pos2))))
    for v, lista in vmarcas.items():
        usos = usos_var.get(v, [])
        compartidos.append((f"Variable `{v}`", [(tipo, txt, f"[L{n}](../help-center/.gitbook/vars.yaml#L{n})") for n, tipo, txt in lista], usos))
        for p, pos in usos:
            tit, ancla = seccion_en(pags[p], pos)
            sec = f"[{tit}]({url_pagina(p)}#{ancla})" if tit else "Inicio de la página"
            for n, tipo, txt in lista:
                por_pagina.setdefault(p, []).append((pos, sec, tipo, f"Variable `{v}`: {txt}", f"[L{n}](../help-center/.gitbook/vars.yaml#L{n})"))

    total_propios = sum(len(marcas(t)) for t in pags.values())
    total_comp = sum(len(c[1]) for c in compartidos)
    cuenta = {}
    for t in list(pags.values()) + list(blqs.values()):
        for _, tipo, _ in marcas(t):
            base = "contradicción" if tipo.startswith("contradicción") else tipo
            cuenta[base] = cuenta.get(base, 0) + 1
    for lista in vmarcas.values():
        for _, tipo, _ in lista:
            base = "contradicción" if tipo.startswith("contradicción") else tipo
            cuenta[base] = cuenta.get(base, 0) + 1

    out = ["# Pendientes del borrador", "",
           "Lista generada por `herramientas/generar_pendientes.py` a partir de los marcadores del contenido. "
           "No se edita a mano: se corrige el marcador y se vuelve a generar. GitBook no importa esta carpeta.", "",
           f"**{total_propios + total_comp} pendientes**: {total_propios} en páginas y {total_comp} en bloques o variables compartidos, "
           f"que se repiten en cada página donde se usan. {len(por_pagina)} páginas afectadas.", "",
           "| Tipo | Qué significa | Número |", "|---|---|---|"]
    for t in ORDEN_TIPOS:
        out.append(f"| {t} | {TIPOS[t]} | {cuenta.get(t, 0)} |")
    out += ["", "## Bloques y variables compartidos", ""]
    if not compartidos:
        out += ["Ninguno.", ""]
    for nombre, lista, usos in sorted(compartidos, key=lambda c: c[0]):
        out += [f"### {nombre}", "", "| Tipo | Pendiente | Línea |", "|---|---|---|"]
        for tipo, txt, enl in sorted(lista, key=lambda x: clave_tipo(x[0])):
            out.append(f"| {tipo} | {celda(txt)} | {enl} |")
        afect = sorted({destino_txt(p, pos) for p, pos in usos}, key=lambda s: s)
        out += ["", "Páginas afectadas: " + ("; ".join(afect) if afect else "ninguna") + ".", ""]
    out += ["## Por página", ""]
    orden = [p for p in menu if p in por_pagina] + sorted(p for p in por_pagina if p not in menu)
    if not orden:
        out += ["Ninguna.", ""]
    for p in orden:
        out += [f"### [{titulo(pags[p]) or p}]({url_pagina(p)})", "", f"`{p}`", "",
                "| Sección | Tipo | Pendiente | Línea |", "|---|---|---|---|"]
        for _, sec, tipo, txt, enl in sorted(por_pagina[p], key=lambda x: x[0]):
            out.append(f"| {sec} | {tipo} | {celda(txt)} | {enl} |")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def main():
    errs = errores_marcas()
    for e in errs:
        print("ERROR  ", e)
    contenido = generar()
    actual = leer(SALIDA) if os.path.exists(SALIDA) else None
    if "--comprobar" in sys.argv:
        if actual != contenido:
            print("DESFASADO  _editorial/pendientes.md · ejecuta: python herramientas/generar_pendientes.py")
            sys.exit(1)
        print("al día     _editorial/pendientes.md")
        sys.exit(1 if errs else 0)
    if actual != contenido:
        escribir(SALIDA, contenido)
        print(f"{'creado' if actual is None else 'actualizado':<10} _editorial/pendientes.md")
    else:
        print("al día     _editorial/pendientes.md")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
