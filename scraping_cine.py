# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
from bs4 import BeautifulSoup
import urllib2
import textwrap


link = "http://cinerama.com.pe"


def cine_url(url=link):
    """Abriendo url pasandoselo a beautifulsoup """
    soup = BeautifulSoup(urllib2.urlopen(url))
    return soup


def eleccion():
    """obteniedoo numero de opcion ingresada por ussuario"""
    click = raw_input("ingresa el numero de enlace que quieres visitar: ")
    click = int(click)-1
    return click


def link_go(diccionario, lista):
    """obtiene la url de que se va a visitar y la imprime"""
    link_click = diccionario[lista[eleccion()]]
    click_url = "{}/{}".format(link, link_click)
    print("Visitando: {}".format(click_url))
    return click_url


#=============barra de navegacion ==================
"""Cometando esta para despues completarla"""
"""soup = cine_url()
print soup.title.string
nav_header = soup.find(attrs={'class': 'menu2'}).findAll('li')
barra_navegacion = {}

for links in nav_header:
    barra_navegacion[str(links.a.text)] = str(links.a['href'])
n = 0
for link_home in barra_navegacion:
    n += 1
    if link_home:
        print("{}.-{}".format(n, link_home))
    else:
        print("Error 404")

lista_a_elegir = barra_navegacion.keys()
click_urls = link_go(barra_navegacion, lista_a_elegir)
"""
#=====================================Ciudades=================================
#===obteniendo todas las ciudades donde esta cinerama y imprimiendolas
soup = cine_url("http://cinerama.com.pe/cines.php")
print("http://cinerama.com.pe/cines.php")
print soup.title.string

encontrar = soup.findAll(attrs={'class': 'cine-lugar'})
lugares = {}
for links in encontrar:
    lugares[str(links.p.text)] = str(links.a['href'])

n = 0
for link_ciudad in lugares:
    n += 1
    if link_ciudad:
        print("{}.-{}".format(n, link_ciudad))
    else:
        print("Error 404")

lista_de_ciudades = lugares.keys()
click_urls_ciudades = link_go(lugares, lista_de_ciudades)


#=================================peliculas====================================
#-*-Abre el link de la ciudad y obtiene los horarios e informacion
soup = cine_url(click_urls_ciudades)
print(soup.title.string)

busca_horario = soup.find(attrs={'class': 'det-cine'})  # <div class='det-cine'>
todo_horario = busca_horario.findAll('div', 'programa')
dias_texto = []

titulo_peli_texto = busca_horario.find('p', 'dtit')
direccion_cine_texto = busca_horario.find('div', 'dtitdire')
print titulo_peli_texto.text
print direccion_cine_texto.find('p').text


def dias():
    """Imprimiendo los dias """
    n = 0
    for dia in dias_texto:
        print(dia.text),
        n += 1
        if n >= 7:
            break


def horario():
    """Imprime los horarios"""
    for hora in horario_texto[1:]:
        for time in hora:
            print(time.text+"/|\\"),
        print("")


def wrapeando():
    """ordenando como se muestra el texto"""
    contenido_texto_wrapeado = textwrap.wrap(contenido_texto, 80)
    print("="*80)
    for lineas in contenido_texto_wrapeado:
        print(lineas)
    print("="*80)


for texto in todo_horario:
    """Buscado titulo, sinopsis, horarios y mas sobre la pelicula"""
    titulo_texto = texto.find('p', 'ptit').text
    contenido_texto = texto.find('p', 'dpel').text
    dias_texto += texto.find_all('td', 'tt', limit=7)
    horario_texto = texto.find_all('tr')
    print(titulo_texto)
    wrapeando()
    dias()
    print("")
    horario()
    print("="*80)
