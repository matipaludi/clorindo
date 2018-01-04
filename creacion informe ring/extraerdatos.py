#!/usr7bin/env python
# -*- coding: utf-8 -*-
import time
import commands
result=commands.getoutput('usr/bin/python pdfajpg.py')

print ('archivo leido aguarde')
promedio = 'Rep' # asigna palabra clave de promedio
minimo = 'Min Warn'
maximo = 'Max Warn'
cdepromedios = 0
cdemax = 0
cdemin = 0
vc = 2 #posiciones teoricas de cada promedio de metal
vsi = 10
vni = 34


linea1 ='1'
linea2 ='2'
linea3 ='3'
cdelinea1 = 0
cdelinea2 = 0
cdelinea3 = 0
a = 0
for linea in file('informe1.txt'): # abre el archivo y lo asigna	
	if linea1 in linea[0]:	
		cdelinea1= cdelinea1 + 1
		if cdelinea1 == 2:
			while a < len(linea):
				if linea[a] == '.' and linea[a-1] == ' ':
					linea = linea[0:a-1] + linea[a:len(linea)]
				a +=1			
			carbono1 = linea[vc:(vc+7)] #revisar si tiene el < o e = l >
			carbono1 = float(carbono1)#paso a numero 
			silicio1 = linea[vsi:(vsi+8)]
			silicio1 = float(silicio1)#paso a numero 
			niquel1 = linea[vni:(vni+8)]
			niquel1 = float(niquel1)#paso a numero
	if linea2 in linea[0]:
		cdelinea2=cdelinea2 + 1
		if cdelinea2 == 1:
			while a < len(linea):
				if linea[a] == '.' and linea[a-1] == ' ':
					linea = linea[0:a-1] + linea[a:len(linea)]
				a +=1						
			carbono2 = linea[vc:(vc+7)] #re el < o e = l >
			carbono2 = float(carbono2)#paso a numero 
			silicio2 = linea[vsi:(vsi+8)]			
			silicio2 = float(silicio2)#paso a numero 
			niquel2 = linea[vni:(vni+8)]			
			niquel2 = float(niquel2)#paso a numero

	if linea3 in linea[0]:
		cdelinea3=cdelinea3 + 1
		if cdelinea3 == 1:
			while a < len(linea):
				if linea[a] == '.' and linea[a-1] == ' ':
					linea = linea[0:a-1] + linea[a:len(linea)]
				a +=1						
			carbono3 = linea[vc:(vc+7)] #revisar si tiene el < o e = l >
			carbono3 = float(carbono3)			
			silicio3 = linea[vsi:(vsi+8)]
			silicio3 = float(silicio3)
			niquel3 = linea[vni:(vni+8)]		
			niquel3 = float(niquel3)#paso a numero


Sc1=carbono1/(4.3 - 0.33 * silicio1 - 0.047 * niquel1 + 0.0055 * niquel1 * silicio1)
Sc2=carbono2/(4.3 - 0.33 * silicio2 - 0.047 * niquel2 + 0.0055 * niquel2 * silicio2)
Sc3=carbono3/(4.3 - 0.33 * silicio3 - 0.047 * niquel3 + 0.0055 * niquel3 * silicio3)


if Sc2 < Sc1 > Sc3:
	maxSc = Sc1
if Sc2 > Sc1 < Sc3:
	minSc = Sc1
if Sc1 > Sc2 < Sc3:
	minSc = Sc2
if Sc1 < Sc2 > Sc3:
	maxSc = Sc2
if Sc1 > Sc3 < Sc2:
	minSc = Sc3
if Sc1 < Sc3 > Sc2:
	maxSc = Sc3

print 'min y max'
maxSc = round(maxSc,2) ('redondeo')
minSc = round(minSc,2)

print maxSc
print minSc

