#!/usr7bin/env python
# -*- coding: utf-8 -*-
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
#print "hello world"
#from PIL import Image
#print "hello world 2 "
#from pytesser import *
#print "3"
import commands
result=commands.getoutput('usr/bin/python pdfajpg.py')

#image_file = 'NIR-0.jpg'
#im = Image.open(image_file)
#print "tomo imagen"
#text = image_to_string(im)
#text = image_to_string(image_file)
#text = image_to_string#(image_file,gracefull_errors=True)
#print "terminado"
#print text

#InformeN= raw_input('introduzca el tipo de informe \n\n 1:.... \n\n 2:....\n\n ')

#print ('peso colada:')
#pesocolada= raw_input("intrduzca el peso de la colada: ") #ingreso de peso de la colada
#print ('peso colada:')
#print pesocolada + ('kg')

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
vc = 4 #posiciones teoricas de cada promedio de metal
vsi = 12
vmg = 20
vcr = 28
vni = 36
vcu = 45
vp  = 52
vs = 4
val = 31
linea1 = 0
linea2 = 0
linea3 = 0
b = 0
for linea in file('informe1.txt'): # abre el archivo y lo asigna	
	if promedio in linea:	
		cdepromedios= cdepromedios + 1
		largo = len(linea)	
		if cdepromedios == 1: #si la linea es la primera de promedio saco lo mas importante
			if (linea[vc] == '>') or (linea[vc]== '<'):#si encuentra un < o > mueve el puntero
					vc += 1
					vsi += 1
					vmg += 1
					vcr += 1
					vni += 1
					vcu += 1
					vp  += 1
					promediocarbono = linea[vc:(vc+7)] #revisar si tiene el < o e = l >
					promediocarbono = float(promediocarbono)#paso a numero 
			else:
					promediocarbono = linea[vc:(vc+7)] #revisar si tiene el < o e = l >
					promediocarbono = float(promediocarbono)#paso a numero
			if (linea[vsi] == '>') or (linea[vsi]== '<'):
					vsi += 1
					vmg += 1
					vcr += 1
					vni += 1
					vcu += 1
					vp  += 1
					promediosilicio = linea[vsi:(vsi+8)]
					promediosilicio = promediosilicio[0] + promediosilicio[2:8] #queda un espacio no se porque	
					promediosilicio = float(promediosilicio)		
			else:
					promediosilicio = linea[vsi:(vsi+8)]
					promediosilicio = promediosilicio[0] + promediosilicio[2:8] #queda un espacio no se porque	
					promediosilicio = float(promediosilicio)
			if (linea[vmg] == '>') or (linea[vmg]== '<'):
					vmg += 1
					vcr += 1
					vni += 1
					vcu += 1
					vp  += 1
					promediomanganeso = linea[vmg:(vmg+7)]
					promediomanganeso = float(promediomanganeso)			
			else:
					promediomanganeso = linea[vmg:(vmg+7)]
					promediomanganeso = float(promediomanganeso)
			if (linea[vcr] == '>') or (linea[vcr]== '<'):
					vcr += 1
					vni += 1
					vcu += 1
					vp  += 1
					promediocromo = linea[vcr:(vcr+8)]
					promediocromo = float(promediocromo)				
			else:	
					promediocromo = linea[vcr:(vcr+8)]
					promediocromo = float(promediocromo)							
			if (linea[vni] == '>') or (linea[vni]== '<'):
					vni += 1
					vcu += 1
					vp  += 1
					promedioniquel = linea[vni:(vni+8)]
					promedioniquel = float(promedioniquel) 			
			else:	
					promedioniquel = linea[vni:(vni+8)]
					promedioniquel = float(promedioniquel) 
			if (linea[vcu] == '>') or (linea[vcu]== '<'):
					vcu += 1
					vp  += 1
					promediocobre = linea[vcu:(vcu+7)]
					promediocobre = float(promediocobre)
			else:
					promediocobre = linea[vcu:(vcu+7)]
					promediocobre = float(promediocobre)
			if (linea[vp] == '>') or (linea[vp]== '<'):
					vp  += 1
					promediofosforo = linea[vp:(vp+8)]
					promediofosforo = float(promediofosforo)
			else:		
					promediofosforo = linea[vp:(vp+8)]
					promediofosforo = float(promediofosforo)
					
		

		elif cdepromedios == 2:
			if linea[vs] == '>' or linea[vs] == '<':			
				vs += 1	
				val += 1			
				promS = linea[vs:(vs+8)]
				promS = float(promS)
			else:
				promS = linea[vs:(vs+8)]
				promS = float(promS)
			if linea[vs + 9] == '>' or linea[vs + 9] == '<':
				val += 1
			if linea[vs + 18] == '>' or linea[vs + 9] == '<':
				val += 1			
			if linea[vs + 27] == '>' or linea[vs + 9] == '<':
				val += 1
				promAl= linea [val:(val+8)]
				promAl = float(promAl)
			else:
				promAl= linea [val:(val+8)]
				promAl = float(promAl)
		elif cdepromedios == 4: #en la linea del hierro guardo el promedio del hierro
			
			promfe = linea [50:58]
			promfe = float(promfe)
		
			
			
	if minimo in linea: #buscamos los minimos permitidos de cada uno 
		cdemin += 1
		if cdemin == 1:      #ver si sumar decimas
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
			minP  = float (minP)		
			
	
	if maximo in linea:
		cdemax += 1
		if cdemax == 1:
			if cdemax == 1: #ver si restar decimas
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
				maxP  = linea [58:66]					
				maxP  = float (maxP)	
		if cdemax == 2: 
				maxAl = linea[36:43]	
				maxAl = float(maxAl)
 
	maxAl1 =0.008
	if linea[0] == '1':
		linea1 += 1
		if linea1 ==3:
			Al1=linea[28:37]
			Al1= float (Al1)
			if Al1 > maxAl1:
				b= 1 
		 
	if linea [0] == '2':
		linea2 += 1
		if linea2 ==2:
			Al2=linea[30:38]
			Al2 = float (Al2)
			if Al2>maxAl1:
				b= 1 
	if linea [0] == '3':
		linea3 += 1
		if linea3 ==2:
			Al3=linea[30:38]
			Al3 = float(Al3)			
			if Al3>maxAl1:
				b= 1 	
print Al1
print Al2
print Al3
if b == 1:
	print 'HAY VALORES ALTOS DE ALUMINIO'
if promAl > maxAl:
	print 'CUIDADO!! ALTOS VALORES DE ALUMINIO'


#-----------Creacion de informe-----------------
doc = canvas.Canvas("reporte3.pdf", pagesize =A4)
doc.drawImage("logo.jpg",5,790, width=100, height=50) #pegado del logo
dia = time.strftime("%d/%m/%y")
doc.setFont("Helvetica", 12) #fuente comun
doc.drawString (200, 750, " Informe de balanceo de NIR del dia " + dia )
doc.line(201,749,443,749) # Subraya
doc.setFont("Helvetica",10)


doc.line(50,700,500,700)
doc.line(50,130,500,130)
doc.line(50,700,50,130)
doc.line(500,700,500,130)
doc.line(150,700,150,130)
doc.line(200,700,200,130)
doc.line(300,700,300,130)
doc.line(400,700,400,130)
doc.line(500,700,500,130)
doc.line(50,670,500,670)
doc.line(50,610,500,610)
doc.line(50,550,500,550)
doc.line(50,490,500,490)
doc.line(50,430,500,430)
doc.line(50,370,500,370)
doc.line(50,310,500,310)
doc.line(50,250,500,250)
doc.line(50,190,500,190)


doc.drawString(60,680, "         Material             Simbolo         Valor Mínimo          Valor Recomendado         Valor Máximo"  )
doc.setFont('Helvetica-Bold',16)
doc.drawString(60,630,"  Carbono       C                                                                        "  )
doc.drawString(60,570,"    Silicio         Si                                                                        "  )
doc.drawString(55,510,"Manganesio   Mn                                                                        "  )
doc.drawString(60,450,"    Cromo        Cr                                                                        "  )
doc.drawString(60,390,"    Niquel         Ni                                                                        "  )
doc.drawString(60,330,"    Cobre         Cu                                                                        "  )
doc.drawString(60,270,"    Hierro         Fe                                                                        "  )
doc.drawString(60,210,"   Fósforo        P                                                                        "  )
doc.drawString(60,150,"    Azufre         S                                                                        "  )

doc.drawString(240,630, str(promediocarbono))
doc.drawString(340,630, str(promediocarbono))
doc.drawString(440,630, str(promediocarbono))


doc.drawString(240,570, str(promediosilicio))
doc.drawString(340,570, str(promediosilicio))
doc.drawString(440,570, str(promediosilicio))
doc.drawString(240,510, str(promediomanganeso))
doc.drawString(340,510, str(promediomanganeso))
doc.drawString(440,510, str(promediomanganeso))
doc.drawString(240,450, str(promediocromo))
doc.drawString(340,450, str(promediocromo))
doc.drawString(440,450, str(promediocromo))
doc.drawString(240,390, str(promedioniquel))
doc.drawString(340,390, str(promedioniquel))
doc.drawString(440,390, str(promedioniquel))
doc.drawString(240,330, str(promediocobre))
doc.drawString(340,330, str(promediocobre))
doc.drawString(440,330, str(promediocobre))
doc.drawString(240,270, str(promediofosforo))
doc.drawString(340,270, str(promediofosforo))
doc.drawString(440,270, str(promediofosforo))
doc.drawString(240,210, str(promfe))
doc.drawString(340,210, str(promfe))
doc.drawString(440,210, str(promfe))
doc.drawString(240,160, str(promS))
doc.drawString(340,160, str(promS))
doc.drawString(440,160, str(promS))

doc.save()





"""
print 'Promedios'			
print promediocarbono
print promediosilicio
print promediomanganeso
print promediocromo
print promedioniquel
print promediocobre
print promediofosforo
print promfe
print promAl
print promS
print 'maximos' 
print maxC
print maxSi
print maxMn
print maxCr
print maxNi
print maxCu
print maxP
print 'minimos'
print minC
print minSi
print minMn
print minCr
print minNi
print minCu
print minP"""
