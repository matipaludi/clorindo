#!/usr7bin/env python

#print "hello world"
#from PIL import Image
#print "hello world 2 "
#from pytesser import *
#print "3"

#image_file = 'NIR-0.jpg'
#im = Image.open(image_file)
#print "tomo imagen"
#text = image_to_string(im)
#text = image_to_string(image_file)
#text = image_to_string#(image_file,gracefull_errors=True)
#print "terminado"
#print text

#import os
#os.system ('tesseract NIR-0.jpg informe1')
#palabra = raw_imput ("palabra a buscar")# pide al usuario que escriba la palabra 
#archivo = open('informe1.txt', 'r')
print ('archivo leido aguarde')
promedio = 'Rep' # asigna palabra clave de promedio
minimo = 'Min Warn'
maximo = 'Max Warn'
cdepromedios = 0
cdemax = 0
cdemin = 0
for linea in file('informe1.txt'): # abre el archivo y lo asigna	
	if promedio in linea:	
		cdepromedios= cdepromedios + 1
		largo = len(linea)		
		if cdepromedios == 1: #si la linea es la primera de promedio saco lo mas importante			
			promediocarbono = linea[5:12] #revisar si tiene el < o e = l >
			promediocarbono = float(promediocarbono)#paso a numero 
			promediosilicio = linea[14:22]
			promediosilicio = promediosilicio[0] + promediosilicio[2:8] #queda un espacio no se porque			
			promediosilicio = float(promediosilicio)
			promediomanganeso = linea[23:30]
			promediomanganeso = float(promediomanganeso)			
			promediocromo = linea[31:39]
			promediocromo = float(promediocromo)			
			promedioniquel = linea[40:47]
			promedioniquel = float(promedioniquel) 			
			promediocobre = linea[48:55]
			promediocobre = float(promediocobre)
			promediofosforo = linea[56:64]
			promediofosforo = float(promediofosforo)
			print 'Promedios'			
			print promediocarbono
			print promediosilicio
			print promediomanganeso
			print promediocromo
			print promedioniquel
			print promediocobre
			print promediofosforo
		elif cdepromedios == 4: #en la linea del hierro guardo el promedio del hierro
			
			promfe = linea [50:58]
			promfe = float(promfe)
			print promfe
	if minimo in linea: #buscamos los minimos permitidos de cada uno 
		cdemin += 1
		if cdemin == 1:
			minC = linea [9:15]
			minC = float (minC)
			minSi = linea [16:22]
			minSi = float (minSi)			
			minMn = linea [25:29]
			minMn = float (minMn)
			minCr = linea [33:36]
			minCr = float (minCr)
			minNi = linea [40:46]
			minNi = float (minNi)
			minCu = linea [50:56]
			minCu = float (minCu)
			minP  = linea [60:66]		
			print 'm' + minP			
			minP  = float (minP)		
			print 'minimos'
			print minC
			print minSi
			print minMn
			print minCr
			print minNi
			print minCu
			print minP
	if maximo in linea:
		cdemax += 1
		if cdemax == 1:
			if cdemax == 1:
				maxC = linea [9:15]
				maxC = float (maxC)
				maxSi = linea [16:22]
				maxSi = float (maxSi)			
				maxMn = linea [25:29]
				maxMn = float (maxMn)
				maxCr = linea [33:36]
				maxCr = float (maxCr)
				maxNi = linea [40:46]
				maxNi = float (maxNi)
				maxCu = linea [50:56]
				maxCu = float (maxCu)
				maxP  = linea [60:66]					
				maxP  = float (maxP)		
				print 'maximos'
				print maxC
				print maxSi
				print maxMn
				print maxCr
				print maxNi
				print maxCu
				print maxP
		print linea
