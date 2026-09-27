"""Genera una vista previa HTML navegable de la sección Personas para revisar en local.

No es GitBook: reproduce la estructura (menú, pestañas, pasos, avisos, tarjetas, bloques
reutilizables y variables) para validar contenido, enlaces y navegación antes de subir.

- Los enlaces propuestos pendientes se muestran resaltados con su identificador (E01…)
  y el motivo al pasar el ratón.
- Los bloques reutilizables se enmarcan con su nombre, para ver dónde se reutilizan.
- revision.html resume la validación, las propuestas de enlace (con casillas para decidir)
  y los puntos pendientes de validar.

Uso: python herramientas/vista_previa.py [--salida CARPETA]
     (por defecto, la carpeta «vista-previa» junto al repositorio)
"""
import html
import json
import os
import re
import shutil
import sys

import markdown
import yaml

sys.path.insert(0, os.path.dirname(__file__))
from comun import EDITORIAL, HC, REPO, bloques, frontmatter, indice, leer, norm, paginas, titulo  # noqa: E402
import aplicar_enlaces  # noqa: E402

SALIDA = os.path.abspath(sys.argv[sys.argv.index("--salida") + 1]) if "--salida" in sys.argv \
    else os.path.abspath(os.path.join(REPO, "..", "vista-previa"))

IDX = indice()
EXTERNOS = IDX.get("externos", {})
PROPUESTAS = aplicar_enlaces.cargar()
PROP_POR_ID = {p["id"]: p for p in PROPUESTAS}
BLOQUES = bloques()
VARS = yaml.safe_load(leer(os.path.join(HC, ".gitbook", "vars.yaml"))) or {}
PAGS = paginas()


# ---------------------------------------------------------------- menú
def leer_menu():
    """[(grupo, [(titulo, destino, externo)])]"""
    grupos, actual = [], ("", [])
    for linea in leer(os.path.join(HC, "SUMMARY.md")).splitlines():
        if linea.startswith("## "):
            if actual[1] or actual[0]:
                grupos.append(actual)
            actual = (linea[3:].strip(), [])
        m = re.match(r'\s*\* \[([^\]]+)\]\(([^)\s]+)(?: "([^"]+)")?\)', linea)
        if m:
            actual[1].append((m.group(3) or m.group(1), m.group(2), m.group(2).startswith("http")))
    grupos.append(actual)
    return grupos


MENU = leer_menu()


# ---------------------------------------------------------------- transformación del markdown
def expandir_includes(texto, pagina, profundidad=0):
    def sustituir(m):
        ruta = norm(os.path.join(os.path.dirname(pagina), m.group(1)))
        if ruta not in BLOQUES or profundidad > 3:
            return f'<div class="error">Bloque reutilizable no encontrado: {html.escape(m.group(1))}</div>'
        fm, cuerpo = frontmatter(BLOQUES[ruta])

        # enlaces del bloque: relativos al bloque → relativos a la página
        def reenlazar(mm):
            destino = mm.group(2)
            if re.match(r"^([a-z]+:|#)", destino):
                return mm.group(0)
            absoluto = norm(os.path.join(os.path.dirname(ruta), destino))
            return mm.group(1) + norm(os.path.relpath(absoluto, os.path.dirname(pagina) or "."))
        cuerpo = re.sub(r'(\]\(|(?:href|src)=")([^)"\s]+)', reenlazar, cuerpo)
        cuerpo = expandir_includes(cuerpo, pagina, profundidad + 1)
        nombre = os.path.basename(ruta)
        return (f'\n\n<div class="include" markdown="1" data-nombre="{nombre}" '
                f'data-titulo="{html.escape(fm.get("title", ""))}">\n\n{cuerpo}\n\n</div>\n\n')
    return re.sub(r'\{% include "([^"]+)" %\}', sustituir, texto)


def bloques_gitbook(texto):
    reglas = [
        (r'\{% hint style="(\w+)" %\}', r'<div class="hint hint-\1" markdown="1">'),
        (r'\{% endhint %\}', '</div>'),
        (r'\{% tabs %\}', '<div class="tabs" markdown="1">'),
        (r'\{% tab title="([^"]*)" %\}', r'<div class="tab" data-title="\1" markdown="1">'),
        (r'\{% endtab %\}', '</div>'),
        (r'\{% endtabs %\}', '</div>'),
        (r'\{% stepper %\}', '<div class="stepper" markdown="1">'),
        (r'\{% step %\}', '<div class="step" markdown="1">'),
        (r'\{% endstep %\}', '</div>'),
        (r'\{% endstepper %\}', '</div>'),
        (r'\{% content-ref url="([^"]*)" %\}', r'<div class="content-ref" markdown="1">'),
        (r'\{% endcontent-ref %\}', '</div>'),
        (r'<details>', '<details markdown="1">'),
        (r'<summary>(.*?)</summary>', r'<summary>\1</summary>'),
    ]
    for patron, repl in reglas:
        texto = re.sub(patron, lambda m: "\n\n" + m.expand(repl) + "\n\n", texto)
    return texto


def variables(texto, fm):
    def valor(m):
        ambito, nombre = m.group(1), m.group(2)
        v = VARS.get(nombre) if ambito == "space" else (fm.get("vars") or {}).get(nombre)
        if v is None:
            return f'<span class="error">{ambito}.vars.{nombre} sin definir</span>'
        return f'<span class="var" title="Variable {ambito}.vars.{nombre}">{html.escape(str(v))}</span>'
    return re.sub(r'<code class="expression">(space|page)\.vars\.(\w+)</code>', valor, texto)


def tarjetas(texto):
    def tabla(m):
        filas = re.findall(r"<tr>(.*?)</tr>", m.group(1), flags=re.S)
        salida = ['<div class="cards">']
        for fila in filas:
            celdas = re.findall(r"<td>(.*?)</td>", fila, flags=re.S)
            if len(celdas) < 4:
                continue
            icono = re.search(r'class="fa-([\w-]+)"', celdas[0])
            destino = re.search(r'href="([^"]+)"', celdas[3])
            salida.append(
                f'<a class="card" href="{destino.group(1) if destino else "#"}">'
                f'<i class="fa-solid fa-{icono.group(1) if icono else "circle"}"></i>'
                f'<span class="card-t">{celdas[1]}</span><span class="card-d">{celdas[2]}</span></a>')
        salida.append("</div>")
        return "\n".join(salida)
    return re.sub(r'<table data-view="cards">.*?<tbody>(.*?)</tbody></table>', tabla, texto, flags=re.S)


def botones(texto):
    def ask(m):
        consulta = re.search(r'data-query="([^"]*)"', m.group(0))
        q = consulta.group(1) if consulta else ""
        nota = f"En GitBook abre el asistente{' con la pregunta: ' + q if q else ''}"
        return f'<button type="button" class="button primary demo" data-nota="{html.escape(nota)}">'
    texto = re.sub(r'<button type="button" class="button primary"[^>]*data-action="ask"[^>]*>', ask, texto)
    texto = re.sub(r'<button type="button" class="button[^"]*"[^>]*data-action="search"[^>]*>',
                   '<button type="button" class="button secondary demo" data-nota="En GitBook abre el buscador">', texto)
    return texto


def enlaces_html(cuerpo_html, pagina):
    """Convierte enlaces .md a .html, marca externos y propuestas."""
    def href(m):
        destino = m.group(1)
        if destino.startswith("http"):
            return f'href="{destino}" target="_blank" rel="noopener" data-externo="1"'
        destino = re.sub(r"\.md(#|$)", r".html\1", destino)
        return f'href="{destino}"'
    cuerpo_html = re.sub(r'href="([^"]+)"', href, cuerpo_html)

    def propuesta(m):
        p = PROP_POR_ID.get(m.group(2))
        if not p:
            return m.group(0)
        info = f'{p["id"]} · {p["criterio"]} · confianza {p["confianza"]}: {p["motivo"]}'
        return f'<a class="propuesto conf-{p["confianza"]}" data-id="{p["id"]}" {m.group(1)} title="{html.escape(info)}">'
    cuerpo_html = re.sub(r'<a ([^>]*?)\s*title="PROPUESTO (E\d+)">', propuesta, cuerpo_html)
    cuerpo_html = re.sub(r'(<a class="propuesto[^"]*" data-id="(E\d+)"[^>]*>.*?</a>)', r'\1<sup class="pid">\2</sup>', cuerpo_html)
    # Etiqueta «Centro de Ayuda actual» para los enlaces que aún van a Scroll
    cuerpo_html = re.sub(r'(<a href="https://soporte-ibermutua-digital\.scroll\.site[^"]*"[^>]*>.*?</a>)',
                         r'\1<span class="scroll" title="Enlace al Centro de Ayuda actual (Scroll)">↗</span>', cuerpo_html)
    return cuerpo_html


def convertir(texto_md):
    texto_md = re.sub(r"^((?:  )+)(?=[*-] |\d+\. )", lambda m: m.group(1) * 2, texto_md, flags=re.M)
    return markdown.markdown(texto_md, extensions=["md_in_html", "tables", "sane_lists", "attr_list"],
                             output_format="html5")


# ---------------------------------------------------------------- plantilla
CSS = """
:root{--p:#00569C;--p2:#0075C9;--t:#1d2733;--t2:#5b6775;--b:#e3e8ee;--bg:#fff;--bg2:#f6f8fa;
--info:#0075C9;--ok:#3F8527;--warn:#A0561A;--err:#C62828}
*{box-sizing:border-box}body{margin:0;font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--t);background:var(--bg)}
.aviso-vp{background:#fff4e5;border-bottom:1px solid #f0c890;padding:6px 16px;font-size:13px;display:flex;gap:16px;flex-wrap:wrap;align-items:center}
.aviso-vp a{color:var(--p)}.aviso-vp label{cursor:pointer}
header{display:flex;align-items:center;gap:12px;padding:12px 24px;border-bottom:1px solid var(--b)}
header .marca{font-weight:700;color:var(--p);font-size:18px;text-decoration:none}
.layout{display:grid;grid-template-columns:270px minmax(0,1fr) 250px;max-width:1400px;margin:0 auto}
nav.menu{border-right:1px solid var(--b);padding:16px;position:sticky;top:0;height:100vh;overflow:auto;font-size:14px}
nav.menu h4{margin:18px 0 4px;font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--t2)}
nav.menu a{display:block;padding:4px 8px;border-radius:6px;color:var(--t);text-decoration:none}
nav.menu a:hover{background:var(--bg2)}nav.menu a.activo{background:#e6f0f8;color:var(--p);font-weight:600}
main{padding:24px 40px 80px;min-width:0}main h1{font-size:30px;line-height:1.25;margin:0 0 6px}
.desc{color:var(--t2);font-size:17px;margin:0 0 24px}
main h2{margin-top:36px;padding-top:8px;border-top:1px solid var(--b)}main h3{margin-bottom:4px}
main a{color:var(--p)}main img{max-width:100%;border:1px solid var(--b);border-radius:8px}
figure{margin:12px 0}figcaption{font-size:13px;color:var(--t2)}figcaption p{margin:0}
a[id]:empty{display:none}
.hint{border-left:4px solid var(--info);background:#eef6fc;padding:10px 16px;border-radius:6px;margin:16px 0}
.hint-warning{border-color:var(--warn);background:#fbf3ec}.hint-success{border-color:var(--ok);background:#eef6ea}.hint-danger{border-color:var(--err);background:#fcecec}
.hint p{margin:6px 0}
.tabs{border:1px solid var(--b);border-radius:8px;margin:16px 0}.tabbar{display:flex;border-bottom:1px solid var(--b);background:var(--bg2);border-radius:8px 8px 0 0}
.tabbar button{border:0;background:none;padding:10px 18px;font:inherit;cursor:pointer;color:var(--t2)}
.tabbar button.on{color:var(--p);box-shadow:inset 0 -2px var(--p);font-weight:600}.tab{padding:4px 20px}.tab.off{display:none}
.stepper{counter-reset:paso;margin:12px 0}.step{counter-increment:paso;position:relative;padding:0 0 12px 44px;border-left:2px solid var(--b);margin-left:14px}
.step:last-child{border-color:transparent}.step::before{content:counter(paso);position:absolute;left:-15px;top:0;width:28px;height:28px;border-radius:50%;
background:var(--p);color:#fff;font-size:14px;display:flex;align-items:center;justify-content:center;font-weight:600}
.step>h3:first-child{margin-top:0;padding-top:1px}
.content-ref a{display:block;border:1px solid var(--b);border-radius:8px;padding:12px 16px;margin:8px 0;text-decoration:none;font-weight:600}
.content-ref a:hover{border-color:var(--p)}.content-ref p{margin:0}
details{border:1px solid var(--b);border-radius:8px;padding:8px 16px;margin:8px 0}summary{cursor:pointer;font-weight:600}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin:20px 0}
.card{border:1px solid var(--b);border-radius:10px;padding:16px;text-decoration:none;color:var(--t);display:flex;flex-direction:column;gap:4px}
.card:hover{border-color:var(--p);box-shadow:0 2px 8px rgba(0,86,156,.12)}.card i{color:var(--p);font-size:22px}.card-t{font-weight:600}.card-d{color:var(--t2);font-size:14px}
.button{display:inline-block;border-radius:8px;padding:8px 16px;font:inherit;font-weight:600;cursor:pointer;text-decoration:none;margin:4px 8px 4px 0}
.button.primary{background:var(--p);color:#fff;border:1px solid var(--p)}.button.secondary{background:#fff;color:var(--p)!important;border:1px solid var(--p)}
table{border-collapse:collapse;margin:12px 0;font-size:15px}th,td{border:1px solid var(--b);padding:6px 10px;text-align:left;vertical-align:top}th{background:var(--bg2)}
.var{background:#eef3f8;border-radius:4px;padding:0 4px;border-bottom:1px dotted var(--p)}
.scroll{font-size:12px;margin-left:2px;color:var(--warn)}
body.marcas .include{outline:1px dashed #9bb7d4;outline-offset:6px;margin:18px 0;position:relative}
body.marcas .include::before{content:"Bloque reutilizable: " attr(data-nombre);position:absolute;top:-17px;right:0;font-size:11px;color:#6b8db0;background:#fff;padding:0 4px}
body.marcas a.propuesto{background:#fff3b0;border-bottom:2px solid #e0b400;text-decoration:none}
body.marcas a.propuesto.conf-media{background:#ffe7c2}body.marcas a.propuesto.conf-baja{background:#ffd6d6;border-color:var(--err)}
.pid{display:none;font-size:10px;color:#8a6d00;margin-left:1px}body.marcas .pid{display:inline}
aside.toc{padding:24px 16px;font-size:13px;position:sticky;top:0;height:100vh;overflow:auto}
aside.toc h4{margin:0 0 6px;font-size:12px;text-transform:uppercase;color:var(--t2)}aside.toc a{display:block;color:var(--t2);text-decoration:none;padding:2px 0}
aside.toc a:hover{color:var(--p)}aside .caja{margin-top:20px;border-top:1px solid var(--b);padding-top:12px}
aside .prop{margin:6px 0;padding:6px;border-radius:6px;background:var(--bg2)}aside .prop b{color:#8a6d00}
.meta{margin-top:48px;font-size:13px;color:var(--t2);border-top:1px dashed var(--b);padding-top:8px}
.error{color:var(--err);font-weight:600}.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:#1d2733;color:#fff;padding:10px 16px;border-radius:8px;font-size:14px;display:none}
@media (max-width:1100px){.layout{grid-template-columns:230px minmax(0,1fr)}aside.toc{display:none}}
@media (max-width:760px){.layout{display:block}nav.menu{position:static;height:auto;border-right:0;border-bottom:1px solid var(--b)}main{padding:16px}}
"""

JS = """
document.querySelectorAll('.tabs').forEach(function(t){var tabs=[].slice.call(t.children).filter(function(c){return c.classList.contains('tab')});
var bar=document.createElement('div');bar.className='tabbar';tabs.forEach(function(tab,i){var b=document.createElement('button');b.textContent=tab.dataset.title;
b.onclick=function(){tabs.forEach(function(x,j){x.classList.toggle('off',j!==i);bar.children[j].classList.toggle('on',j===i)})};bar.appendChild(b);if(i)tab.classList.add('off');else b.classList.add('on')});
t.insertBefore(bar,t.firstChild)});
function irAncla(){if(!location.hash)return;var el=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!el)return;
var tab=el.closest('.tab');if(tab&&tab.classList.contains('off')){var t=tab.parentNode,tabs=[].slice.call(t.querySelectorAll(':scope>.tab'));
t.querySelector('.tabbar').children[tabs.indexOf(tab)].click()}setTimeout(function(){(el.closest('h1,h2,h3,h4')||el).scrollIntoView()},30)}
window.addEventListener('hashchange',irAncla);irAncla();
var toast=document.querySelector('.toast');document.querySelectorAll('.demo').forEach(function(b){b.onclick=function(){toast.textContent=b.dataset.nota+' (no disponible en la vista previa).';toast.style.display='block';setTimeout(function(){toast.style.display='none'},3500)}});
var cb=document.getElementById('marcas');if(cb){var k='vp-marcas';try{if(localStorage.getItem(k)==='0'){cb.checked=false}}catch(e){}
function ap(){document.body.classList.toggle('marcas',cb.checked);try{localStorage.setItem(k,cb.checked?'1':'0')}catch(e){}}cb.onchange=ap;ap()}
"""

FA = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">'


def menu_html(pagina):
    raiz = norm(os.path.relpath(".", os.path.dirname(pagina) or "."))
    pre = "" if raiz == "." else raiz + "/"
    partes = []
    for grupo, entradas in MENU:
        if grupo:
            partes.append(f"<h4>{html.escape(grupo)}</h4>")
        for t, destino, externo in entradas:
            if externo:
                partes.append(f'<a href="{destino}" target="_blank" rel="noopener">{html.escape(t)} <span class="scroll">↗</span></a>')
            else:
                clase = ' class="activo"' if destino == pagina else ""
                partes.append(f'<a{clase} href="{pre}{destino[:-3]}.html">{html.escape(t)}</a>')
    return "\n".join(partes), pre


def plantilla(titulo_pag, cuerpo, pagina, lateral=""):
    menu, pre = menu_html(pagina)
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titulo_pag)} · Vista previa</title>{FA}<style>{CSS}</style></head><body class="marcas">
<div class="aviso-vp"><b>Vista previa local</b> — no es GitBook; los estilos son aproximados.
<label><input type="checkbox" id="marcas" checked> Mostrar enlaces propuestos y bloques reutilizables</label>
<a href="{pre}revision.html">Revisión del piloto</a></div>
<header><a class="marca" href="{pre}README.html">Ayuda de Ibermutua Digital · Personas</a></header>
<div class="layout"><nav class="menu">{menu}</nav><main>{cuerpo}</main><aside class="toc">{lateral}</aside></div>
<div class="toast"></div><script>{JS}</script></body></html>"""


# ---------------------------------------------------------------- páginas
def render_pagina(pagina, texto):
    propias = [p for p in PROPUESTAS if p["pagina"] == pagina and p["estado"] in ("propuesto", "aceptado")]
    no_aplicables = []
    for p in propias:
        texto, problema = aplicar_enlaces.aplicar(texto, p, EXTERNOS, marcar=True)
        if problema:
            no_aplicables.append((p, problema))
    fm, cuerpo = frontmatter(texto)
    cuerpo = expandir_includes(cuerpo, pagina)
    cuerpo = variables(cuerpo, fm)
    cuerpo = tarjetas(cuerpo)
    cuerpo = botones(cuerpo)
    cuerpo = bloques_gitbook(cuerpo)
    h = convertir(cuerpo)
    if fm.get("description"):
        h = re.sub(r"(</h1>)", r'\1<p class="desc">' + html.escape(str(fm["description"]).strip()) + "</p>", h, count=1)
    h = enlaces_html(h, pagina)
    datos = IDX["paginas"].get(pagina, {})
    temas = ", ".join(IDX["temas"].get(t, t) for t in datos.get("temas", []))
    resuelve = "; ".join(r["intencion"] + (f' (#{r["ancla"]})' if r["ancla"] else "") for r in datos.get("resuelve", []))
    h += (f'<div class="meta">Tipo: {datos.get("tipo", "—")} · Temas: {temas or "—"}'
          f'{" · Preguntas frecuentes: " + IDX["temas"][datos["faq_tema"]] if datos.get("faq_tema") else ""}'
          f'<br>Resuelve: {html.escape(resuelve) or "—"}<br>Archivo: help-center/{pagina}</div>')
    # lateral: índice de la página y propuestas
    toc = re.findall(r'<h2[^>]*>(.*?)</h2>', h)
    lateral = "<h4>En esta página</h4>"
    for t in toc:
        ancla = re.search(r'id="([^"]+)"', t)
        limpio = re.sub(r"<[^>]+>", "", t)
        if ancla:
            lateral += f'<a href="#{ancla.group(1)}">{limpio}</a>'
    if propias:
        lateral += f'<div class="caja"><h4>Enlaces propuestos ({len(propias)})</h4>'
        for p in propias:
            destino = nombre_destino(p)
            lateral += (f'<div class="prop"><b>{p["id"]}</b> · {p["criterio"]} · {p["confianza"]}<br>'
                        f'«{html.escape(p.get("texto", p["buscar"]) if p["tipo"] == "enlazar" else "frase nueva")}» → {html.escape(destino)}</div>')
        for p, problema in no_aplicables:
            lateral += f'<div class="prop error">{p["id"]}: {html.escape(problema)}</div>'
        lateral += "</div>"
    return plantilla(fm.get("title") or titulo(texto), h, pagina, lateral)


def nombre_destino(p):
    if p["destino"].startswith("externo:"):
        return EXTERNOS[p["destino"][8:]]["intencion"].capitalize() + " ↗"
    ruta, _, ancla = p["destino"].partition("#")
    destino = norm(os.path.join(os.path.dirname(p["pagina"]), ruta))
    t = titulo(PAGS.get(destino, ""))
    if ancla:
        m = re.search(r"^#+ (.+?) <a href=\"#" + re.escape(ancla) + '"', PAGS.get(destino, ""), flags=re.M)
        t += " › " + (m.group(1) if m else "#" + ancla)
    return t


# ---------------------------------------------------------------- revisión
def render_revision():
    import validar  # se ejecuta al importar
    r = validar.RESUMEN
    partes = [f"<h1>Revisión del piloto</h1><p class='desc'>Generada con herramientas/vista_previa.py a partir de la rama local.</p>"]
    partes.append("<h2>Validación automática</h2>")
    partes.append(f"<p>{r['paginas']} páginas · {r['bloques']} bloques reutilizables · {r['variables']} variables · "
                  f"{r['catalogo']} enlaces del catálogo contextual · {r['propuestas']} enlaces propuestos ({r['pendientes']} pendientes).</p>")
    if r["errores"]:
        partes.append("<div class='hint hint-danger'><p><b>Errores</b></p><ul>" + "".join(f"<li>{html.escape(e)}</li>" for e in r["errores"]) + "</ul></div>")
    else:
        partes.append("<div class='hint hint-success'><p><b>Sin errores.</b> Menú, enlaces, anclas, imágenes, bloques, variables, índice y preguntas frecuentes coherentes.</p></div>")
    if r["avisos"]:
        partes.append("<ul>" + "".join(f"<li>{html.escape(a)}</li>" for a in r["avisos"]) + "</ul>")

    partes.append("<h2 id='enlaces'>Enlaces por intención</h2><p>Marca las que aceptas y pulsa <b>Copiar decisión</b> para pegarla en el chat. "
                  "Amarillo = confianza alta; naranja = media; rojo = baja.</p>")
    filas = []
    for p in PROPUESTAS:
        destino = nombre_destino(p)
        pag_html = p["pagina"][:-3] + ".html"
        texto = p.get("texto", p["buscar"]) if p["tipo"] == "enlazar" else "Añadir: " + re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", (p.get("insertar_antes") or p.get("insertar_despues")).strip())
        marcado = "checked" if p["confianza"] in ("alta", "media") and p["estado"] != "rechazado" else ""
        estado = "" if p["estado"] in ("propuesto", "aceptado") else f" ({p['estado']})"
        filas.append(f"<tr class='conf-{p['confianza']}'><td><input type='checkbox' class='dec' value='{p['id']}' {marcado}></td><td><b>{p['id']}</b>{estado}</td>"
                     f"<td><a href='{pag_html}'>{html.escape(titulo(PAGS[p['pagina']]))}</a></td><td>«{html.escape(texto)}»</td><td>{html.escape(destino)}</td>"
                     f"<td>{p['criterio']}<br><small>{html.escape(p['motivo'])}</small></td><td>{p['confianza']}</td></tr>")
    partes.append("<table><tr><th></th><th>Id</th><th>Página</th><th>Texto enlazado</th><th>Destino</th><th>Criterio y motivo</th><th>Confianza</th></tr>"
                  + "".join(filas) + "</table>")
    partes.append("<p><button class='button primary' id='copiar'>Copiar decisión</button> <span id='copiado'></span></p>"
                  "<textarea id='decision' rows='3' style='width:100%;font:13px monospace' readonly></textarea>")

    pend = os.path.join(EDITORIAL, "revision-piloto.md")
    if os.path.exists(pend):
        partes.append(markdown.markdown(leer(pend), extensions=["tables", "sane_lists"]))
    js = """<script>function dec(){var a=[],r=[];document.querySelectorAll('.dec').forEach(function(c){(c.checked?a:r).push(c.value)});
var t='Enlaces: aceptar '+(a.join(', ')||'ninguno')+'; rechazar '+(r.join(', ')||'ninguno')+'.';document.getElementById('decision').value=t;return t}
document.querySelectorAll('.dec').forEach(function(c){c.onchange=dec});dec();
document.getElementById('copiar').onclick=function(){var t=dec();var ok=function(){document.getElementById('copiado').textContent='Copiado.'};
if(navigator.clipboard){navigator.clipboard.writeText(t).then(ok,function(){document.getElementById('decision').select()})}else{document.getElementById('decision').select()}}</script>
<style>tr.conf-alta td:nth-child(4){background:#fff3b0}tr.conf-media td:nth-child(4){background:#ffe7c2}tr.conf-baja td:nth-child(4){background:#ffd6d6}</style>"""
    return plantilla("Revisión del piloto", "\n".join(partes) + js, "revision.md")


def main():
    os.makedirs(SALIDA, exist_ok=True)
    usadas = set()
    for pagina, texto in PAGS.items():
        destino = os.path.join(SALIDA, pagina[:-3] + ".html")
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        contenido = render_pagina(pagina, texto)
        usadas |= set(re.findall(r'src="[./]*\.gitbook/assets/([^"]+)"', contenido))
        with open(destino, "w", encoding="utf-8", newline="\n") as f:
            f.write(contenido)
    assets = os.path.join(SALIDA, ".gitbook", "assets")
    os.makedirs(assets, exist_ok=True)
    for a in usadas:
        origen = os.path.join(HC, ".gitbook", "assets", a)
        if os.path.exists(origen):
            shutil.copyfile(origen, os.path.join(assets, a))
    with open(os.path.join(SALIDA, "revision.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(render_revision())
    with open(os.path.join(SALIDA, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=README.html"><a href="README.html">Abrir</a>')
    print(f"Vista previa: {len(PAGS)} páginas y {len(usadas)} imágenes en {SALIDA}")
    print(f"Abre {os.path.join(SALIDA, 'index.html')}")


if __name__ == "__main__":
    main()
