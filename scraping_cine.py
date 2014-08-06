# -*- coding: utf-8 *-*
__author__ = 'jenriqueps'
from bs4 import BeautifulSoup
import urllib2

link = "http://cinerama.com.pe"
def cine_url(url=link):
    soup = BeautifulSoup(urllib2.urlopen(url))
    return soup

soup = cine_url()
print soup.title.string
nav_header = soup.find(attrs={'class': 'menu2'}).findAll('li')
barra_navegacion = {}

for links in nav_header:
    barra_navegacion[str(links.a.text)] = str(links.a['href'])

n = 0

for link_home in barra_navegacion:
    n += 1
    if link_home:
        print("{}.-{}".format(n,link_home))
    else:
        print("Error 404")

click = raw_input("ingresa el numero de enlace que quieres visitar: ")
lista_a_elegir =  barra_navegacion.keys()
click = int(click) - 1
link_click = barra_navegacion[lista_a_elegir[click]]
click_url = "{}/{}".format(link, link_click)
print("Visitando: {}".format(click_url))

soup = cine_url(click_url)
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

ciudad_click = raw_input("ingresa el numero de enlace que quieres visitar: ")
lista_de_ciudades =  lugares.keys()
ciudad_click = int(ciudad_click) - 1
ciudad = lugares[lista_de_ciudades[ciudad_click]]
click_url_ciudad = "{}/{}".format(link,ciudad)
print("Visitando: {}".format(click_url_ciudad))
# # data = urlfetch.fetch(urleica, deadline=90).content

soup  = cine_url(click_url_ciudad)
print(soup.title.string)

busca_horario = soup.find(attrs={'class': 'dtitdire'}).findAll("tr")
horario_fila = []
n=0

for tr in busca_horario:
    lista=[]
    td = tr.findAll("td")
    n += 1
    for texto in td:
        lista += [texto.text]
    horario_fila.append(lista)

for titulos in horario_fila:
    for filas in titulos:
        print("%s"%filas),
    print ""
