
############################################################
#                                                          #
# Autor: Hacker Depressivo                                 #
# Data: 21/06/2020                                         #
# Versão: 1.0                                              #
# API documentation - http://ip-api.com/docs/              #
#                                                          #
# YouTube - www.youtube.com/hackerdepressivo               #
############################################################


#!/usr/bin/ env python

# Importando bibliotecas

import requests
import pyfiglet


from pyfiglet import Figlet
v = Figlet(font='big')
print (v.renderText('Hacker Depressivo'))



#Entrada de dados com uma condição!

IP_input = input("Por favor, digite o IP: ")

if len(IP_input) <= 8:
    exit() 


# Requisitando informações na API

request = requests.get('http://ip-api.com/json/{}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'.format(IP_input))

# Armazenando os dados da requisição na váriavel data

data =  (request.json())

print('País: {}'.format(data['country']))
print('------------------------------------------------')
print('Região: {}'.format(data['region']))
print('------------------------------------------------')
print('Localidade: {}'.format(data['regionName']))
print('------------------------------------------------')
print('Cidade: {}'.format(data['city']))
print('------------------------------------------------')
print('Latitude: {}'.format(data['lat']))
print('------------------------------------------------')
print('Longitude: {}'.format(data['lon']))
print('------------------------------------------------')
print('Organização: {}'.format(data['org']))
print('------------------------------------------------')
