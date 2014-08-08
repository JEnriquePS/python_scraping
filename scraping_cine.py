# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
from bs4 import BeautifulSoup
import urllib2


link = "http://cinerama.com.pe/"


def cine_url(url=link):
    soup = BeautifulSoup(urllib2.urlopen(url))
    return soup


def eleccion():
    click = raw_input("ingresa el numero de enlace que quieres visitar: ")
    click = int(click)-1
    return click


def link_go(diccionario, lista):
    link_click = diccionario[lista[eleccion()]]
    click_url = click_url = "{}/{}".format(link, link_click)
    print("Visitando: {}".format(click_url))
    return click_url

#=============barra de navegacion ==================
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
#=============Ciudades=================
soup = cine_url("http://cinerama.com.pe/cines.php")
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


#==================peliculas========================

soup = cine_url(click_urls_ciudades)
print(soup.title.string)


busca_horario = soup.find(attrs={'class': 'det-cine'})
horario_fila = []
titulo_peli={}
uno = busca_horario.findAll('div', 'programa')
hora_peli = busca_horario.findAll('div', 'programa-des')

print len(uno)
dias_texto = []


def dias():
    n = 0
    for dia in dias_texto:
        print(dia.text),
        n += 1
        if n >=7:
            break


def horario():
    for hora in horario_texto[1:]:
        for time in hora:
            print(time.text+"/|\\"),
        print("")


for uns in uno:
    titulo_texto = uns.find('p', 'ptit').text
    contenido_texto = uns.find('p', 'dpel').text
    dias_texto += uns.find_all('td', 'tt', limit=7)
    horario_texto = uns.find_all('tr')
    print(titulo_texto)
    print(contenido_texto)
    dias()
    print("")
    horario()
    print("")

