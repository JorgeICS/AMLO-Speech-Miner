# -*- coding: utf-8 -*-
"""
Creado por Jorge Carrera Septiembre 2024
"""

import requests
from bs4 import BeautifulSoup

# Función para obtener los enlaces de una sola página
def obtener_links_pagina(url):
    response = requests.get(url, verify=False)  # Desactiva la verificación del certificado SSL
    soup = BeautifulSoup(response.content, 'html.parser')

    # Busca los enlaces de los artículos dentro de las etiquetas <h2> o <article>
    links = []
    for article in soup.find_all('article'):
        enlace = article.find('a', href=True)
        if enlace:
            links.append(enlace['href'])
    return links

# Función principal para iterar a través de todas las páginas
def obtener_todos_los_links(paginas=287):
    base_url = "https://amlo.presidente.gob.mx/sala-de-prensa/transcripciones/page/"
    todos_los_links = []

    for i in range(1, paginas + 1):
        url = base_url + str(i) + "/"
        print(f"Obteniendo enlaces de: {url}")
        links = obtener_links_pagina(url)
        todos_los_links.extend(links)

    return todos_los_links

# Obtener todos los enlaces de las 287 páginas
enlaces_articulos = obtener_todos_los_links()

# Imprimir o guardar los enlaces
for enlace in enlaces_articulos:
    print(enlace)
