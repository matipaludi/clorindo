#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import green
import json
doc = canvas.Canvas("reportecalidad.pdf", pagesize =A4) 
#embarque = raw_input('introduzca el numero de embarque')
print "Elija la opcion deseada y luego presione enter"
print "1: para recepcion de muestras"
print "2: para Embarques, orden de compras"
print "3: para PPAP - O.C."
x = raw_input('Elija la opccion: ')
if x == '1':
	doc.drawString(538,709, 'X')
elif x == '2':
	doc.drawString(538,669, 'X')
elif x == '3':
	doc.drawString(538,619, 'X')
else:
	print 'Debe ser un numero del 1 al 3'	
	while int(x) > 3:
		x = raw_input('Elija una opcion entre 1 y 3: ') 
		if x == '1':
			doc.drawString(538,709, 'X')
		elif x == '2':
			doc.drawString(538,669, 'X')
		elif x == '3':
			doc.drawString(538,629, 'X')

embarque = 4001453
#cliente = raw_input ("Ingrese el nombre del cliente:")
cliente = 'KSU'
#nombre = raw_input(' Introduzca el nombre de la persona a cargo del reporte ')

nombre = 'Soperez Leonardo'
turno = 'A' # ver si el turno depende de la hora
#-----------constantes--------------------
with open("constante.json") as g:
	c = json.load(g)
cresistencia= c[0]#constante
calargamiento = c[1]
cdilatacionT = c[2]
cresistencia= cresistencia['resistenciatraccion']
calargamiento = calargamiento['alargamiento']
cdilatacionT = cdilatacionT['coeficientetermica']

fechacolada = time.strftime("%d/%m/%y") # no es la del dia
fechahoy = time.strftime("%d/%m/%y") # ver si es la fecha del dia

#-----------Sombreado-------------------------------------------

doc.setFillColorRGB(0.8,0.8,0.8) #Color Sombreado
doc.roundRect(30,755,520,35,1, stroke  = 1,fill = 1)  # Realizar sombreado (0 sin relleno sin trazo, 1 con)
doc.roundRect(30,502,520,88,1, stroke  = 1,fill = 1)  
doc.roundRect(30,480,70,22,1, stroke  = 1,fill = 1)  
doc.roundRect(30,350,70,20,1, stroke  = 1,fill = 1)   
doc.roundRect(30,180,70,25,1, stroke  = 1,fill = 1)   
doc.roundRect(320,730,230,20,1, stroke  = 1,fill = 1) 
doc.setFillColorRGB(0,0,0)


#----------ciclo muestras--------------------------------
cant = raw_input('Intruduzca la cantidad de muestras:   ')
cantidad = int(cant)
c = 0
if (cantidad > 0) and (cantidad <= 5):
	while c < cantidad:
		doc.setFont("Helvetica", 8)		
		cc = c + 1
		#modelo = raw_input('Ingrese el modelo ' + str(cc) + '  :   ')	
		pmodelo = c*70 + 190		
		#doc.drawString(pmodelo,547, modelo)		
		#fechacolada = raw_input('Ingrese la fecha de colada' + str(cc) +'  :   ')
		#doc.drawString(pmodelo,520,fechacolada)
		#turno = raw_input('Ingrese el turno ' + str(cc) + ' :    ')
		pturno  = c*70 + 197
		#doc.drawString(pturno,510,turno)			
		A = raw_input('Ingrese el valor de "A" sin el simbolo de %: ')
		if A.isdigit() == True :
			pA  = c*70 + 197
			doc.drawString(pA,342,A + '%')
		else: 
			print 'Debe ser un numero'
			continue	
		B = raw_input('Ingrese el valor de "B" sin el simbolo de %: ')
		if B.isdigit() == True:
			doc.drawString(pA,322, B + '%')
			CA = raw_input('Ingrese N para: "NOT PRESENT", o S para: "PRESENT": ')
		else: 
			print 'Debe ser un numero'
			continue	
		psard= c*72 + 187		
		if CA == 'N' or CA=='n' or CA=='NO' or CA=='no' or CA=='No':
				doc.drawString(psard,302, 'NOT')
				doc.drawString(psard,292, 'PRESENT')
		elif CA=='s' or CA == 'S' or CA == 'si' or CA=='SI' or CA=='Si':
				doc.drawString(psard,297, 'PRESENT')	
		else: 
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo			
		D = raw_input('Ingrese el valor de "D" sin el simbolo de %: ')		
		if D.isdigit() == True:		
			doc.drawString(pA,282, D + '%')		
		else: 
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo			
		E = raw_input('Ingrese el valor de "E" sin el simbolo de %: ')
		if E.isdigit() == True:		
			doc.drawString(pA,262, E + '%')
		else: 
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo			
	
		
		Qty= raw_input('Ingrese el valor del porcentaje de carburos (sin el simbolo de %): ')
		if Qty.isdigit() == True:						
			doc.drawString(pA,242, Qty + '%')
		else: 
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo					
		psard   = c*72 + 187			
		doc.drawString(psard,223, 'Small and')
		doc.drawString(psard,215, 'Randomly')
		doc.drawString(psard,207, 'Dispersed')
		Min = raw_input('Ingrese el valor minimo de dureza sin la unidad de medida "HB": ')		
		if Min.isdigit() == True:		
			doc.drawString(pA,185,Min + 'HB')
		else:
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo					
			
		Max = raw_input('Ingrese el valor maximo de dureza sin la unidad de medida "HB": ')
		if Max.isdigit() == True:		
			doc.drawString(pA,185,Min + 'HB')
		else:
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo					
			
		doc.drawString(pA,165,Max + 'HB')
				
		Promedio = raw_input('Ingrese el valor promedio de dureza sin la unidad de medida "HB" : ')
		if Promedio.isdigit() == True:
			doc.drawString(pA,140,Promedio + 'HB')
		else:	
			print 'ERROR: Debe ser un valor numerico'			
			continue #Si no coloca S o N o los errores salvados vuelve a ejectuar de nuevo el ciclo					
			

		c += 1 # suma contador delciclo


#-----------------------VARIABLES------------------------
doc.setFont("Helvetica-Bold", 11) # letra negrita
doc.drawString(402,660,"N°: " + str(embarque))
doc.setFont("Helvetica-Bold", 7)
doc.setFont("Helvetica", 9)
doc.drawString(130,700, cliente)
#color letra        
#doc.setFillColorRGB(0,10,0.9)


#--------------------------------------------------------------------


#---------------------------------------------------------
#Encabezado
doc.drawImage("logo.jpg",40,760, width=50, height=25)#logo
doc.setFont("Helvetica-Bold",25) #letra titulo 1
doc.drawString(150,792, "CLORINDO APPO S.R.L") #TITULO 1
doc.setFont("Helvetica-Bold", 15) #letra titulo 2
doc.drawString(140,775, "REPORTE DE CALIDAD DEL MATERIAL")# TITULO 2
doc.drawString(170,760, "(MATERIAL QUALITY REPORT)")
#-------------CUADRO 1----------------------------------------
reporte = time.strftime("%d%m%y")
doc.setFont("Helvetica-Bold", 11) # letra negrita
doc.drawString(318,735, " Reporte N°/                        " + reporte + ' - ')

doc.drawString(31,718, "Cliente:")
doc.drawString(252,718, "Nombre de Parte")
doc.drawString(402,718, "Recepcion Muestras")
doc.drawString(31,680, "Cant. Mtras Controladas      --------")
doc.drawString(252,680,"Origen Muestra")
doc.drawString(270,660, "Clorindo Appó S.R.L.")
doc.drawString(402,680,"Embarques           O.C")
doc.drawString(31,638, "Total Mtras. Enviadas    ------")
doc.drawString(252,638, "Material")
doc.drawString(287,618,"Ni Resist")
doc.drawString(402,638, "PPAP-O.C.")
doc.drawString(402,614, "N°:")
#Sin Negrita
doc.setFont("Helvetica", 9)
doc.drawString(382,735, "Report Nr.")
doc.drawString(77,718, "(Customer)")
doc.drawString(341,718, "(Part Name)")
doc.drawString(402,698, "(Sample Receiving)")
doc.drawString(31,660, "(Qty of Controlled Samples)")
doc.drawString(335,680, "(Sample)")
doc.drawString(31,615, "(Total Sent Samples)")
doc.drawString(297,638, "(Material)")
doc.drawString(458,638, "(P.O.)")
doc.setFont("Helvetica-Bold", 10)
doc.setFont("Helvetica",6)
doc.drawString(463,680, "(Shipment)/              (P.O.)")

#--------------------CUADRO 2-------------------------------
doc.setFont("Helvetica-Bold", 8)
doc.drawString(31,546, "TIPO DE ENSAYO")
doc.drawString(105,578, "ESPECIFIACION")
doc.drawString(105,566, "   MATERIAL")
doc.drawString(105,526, "  AGV - 700.001")
doc.drawString(300,580,"RESULTADO DEL ENSAYO")
doc.drawString(521,546, "OK")
doc.drawString(536,550, "NO")
doc.drawString(536,538, "OK")

doc.setFont("Helvetica-Bold", 7)
doc.drawString(270,537, "Fecha Colada                                     Turno")

doc.setFont("Helvetica", 8)
doc.drawString(32,340,"Grafito (% tamaño)")
doc.drawString(32,332,"Graphite (% size)")

doc.setFont("Helvetica-Bold", 10)
doc.drawString(132,336, "A")
doc.drawString(132,316, "B")
doc.drawString(132,296, "C")
doc.drawString(132,276, "D")
doc.drawString(132,256, "E")
doc.setFont("Helvetica-Bold",8)
doc.drawString(32,320,"A- (50% Min)")
doc.drawString(32,308,"B- (10% Máx)")
doc.drawString(32,297,"C- No admisible)")
doc.drawString(32,279,"D- (10% Máx)")
doc.drawString(32,270,"E- (20% Máx)")
doc.drawString(32,260,"Tamaño")
doc.drawString(32,253,"4 - 7 ASTM")
doc.drawString(36,487, "25")
doc.drawString(32,150, "120 to 160 HB")
doc.drawString(125,190, "Min.")
doc.drawString(125,164, "Máx.")
doc.drawString(115,148, "Promedio")
doc.drawString(36,356, "26")
doc.setFont("Helvetica",8)
doc.drawString(36,187,"27")

doc.setFont("Helvetica",8)
doc.drawString(105,122,"Ver Adjunto reporte dureza/                                                          ----------------")
doc.setFont("Helvetica",7)
doc.drawString(207,122,"see enclosed hardness report")


doc.setFont("Helvetica", 7)
doc.drawString(32,289,"(Not Permissible)")

doc.drawString(102,219,"Tamaño/Distribución")
doc.drawString(115,209,"(Size/Distrib.)")
doc.setFont("Helvetica-Bold", 7)
doc.drawString(66,242," 5% Máx.")
doc.setFont("Helvetica-Bold", 6)
doc.drawString(32,223,"Finos y Uniformente")
doc.drawString(32,216,"distribuidos")
doc.setFont("Helvetica", 6)
doc.drawString(67,216,"(Small and")
doc.drawString(32,208,"Randomly Disperesed)")
doc.setFont("Helvetica", 8)
doc.drawString(33,242,"Carburos                       Cantidad")
doc.drawString(32,234,"(Carbides)                       (Qty.)")

doc.drawString(104,540, "SPECIFICATION)")
doc.drawString(104,553, "  (MATERIAL")
doc.drawString(31,536," (TYPE OF TEST)")
doc.drawString(320,572, "(TEST RESULTT)")
doc.setFont("Helvetica", 11)
doc.drawString (190,425,"Ver Adjunto Lectura Espectro/ See Enclosed Spectro Issue")
doc.drawString (105,484, "C:")
doc.drawString (105,467, "Si:")
doc.drawString (101,452, "Mn:")
doc.drawString (103,436, "Cr:")
doc.drawString (103,420, "Ni:")
doc.drawString (101,405, "Cu:")
doc.drawString (105,390, "P:")
doc.drawString (105,375, "S:")
doc.setFont("Helvetica",7)
doc.drawString (124,485, "2,30 - 3,00%")
doc.drawString (124,467, "1,50 - 2,50%")
doc.drawString (124,452, "0,80 - 1,50%")
doc.drawString (124,436, "1,00 - 1,60%")
doc.drawString (121,420, "13,50 - 17,00%")
doc.drawString (124,405, "5,00 - 7,00%")
doc.drawString (124,390, "0,10% Máx")
doc.drawString(124,375, "0,10% Máx.")
doc.drawString(105,363,"Matriz Austenitica                   Control Superficial")
doc.drawString(105,353,"Austenitic Matrix                    (Surface Controlj - Overlaping)   ")
doc.drawString(354,358,"O.K.             NO  O.K.")
#doc.setStrokefColorRGB(0.0,1,0.0) # color de trazo
#doc.setFillColorRGB(0,0.0,0.5)# Color de relleno
doc.roundRect(370,353,15,15,1, stroke  = 1,fill = 0) # Realizar  cuadrado (0 sin relleno sin trazo, 1 con)
doc.roundRect(425,353,15,15,1)
doc.setFont("Helvetica-Bold",10)
doc.drawString(374,357,"X")
doc.setFont("Helvetica-Bold", 7)
doc.drawString(58,197,"DUREZA")
doc.drawString(58,492,"QUIMICO")
doc.drawString(51,362, "ESTRUCTURA")
doc.drawString(190,562, "Modelo")
doc.drawString(260,562, "Modelo")
doc.drawString(330,562, "Modelo")
doc.drawString(400,562, "Modelo")
doc.drawString(470,562, "Modelo")
doc.setFont("Helvetica", 7)
doc.drawString(319,537, "(Casting Date)/                       (Shift)")
doc.drawString(53,185,"(HARDNESS)")
doc.drawString(54,482,"(CHEMICAL)")
doc.drawString(52,352,"(STRUCTURE)")
doc.drawString(119,140,"(Average)")
doc.drawString(189,556,"(Part nr)")
doc.drawString(259,556,"(Part nr)")
doc.drawString(329,556,"(Part nr)")
doc.drawString(399,556,"(Part nr)")
doc.drawString(469,556,"(Part nr)")


doc.setFont("Helvetica-Bold",8)
doc.drawString(30,110,"NOTAS/NOTES: Metodo de Control de Dureza (Hardness Control Methond)")
doc.drawString(30,100,"Brinell:                          Ø2,5mm                               187,50 kgs. // Rockwell B:                              Ø1/16'',                        100kgs")
doc.drawString(30,90, "Resistencia a la traccion: (N/mm2)                                                                     >= 150                          " +  str(cresistencia) + "                                        X")
doc.drawString(30,82,"(Tensile Strength)") 
doc.drawString(30,72, "Alargamiento (%)                                                                                                  >= 1                              " +  str(calargamiento)  +"                                         X")
doc.drawString(30,64, "(Enlongation)")
doc.drawString(30,54, "Coeficiente de Dilatacion Térmica: (10E-6/°C)                                                   >= 18,6                         " + str(cdilatacionT) + "                                       X")
doc.drawString(30,44, "Heat Enlogation Coeficient 20 to 300 °C)")
doc.roundRect(495,50,14,14,1, stroke  = 1,fill = 0) # Realizar  cuadrado (0 sin relleno sin trazo, 1 con)
doc.roundRect(530,50,14,14,1)
doc.roundRect(495,68,14,14,1, stroke  = 1,fill = 0) # Realizar  cuadrado (0 sin relleno sin trazo, 1 con)
doc.roundRect(530,68,14,14,1)
doc.roundRect(495,86,14,14,1, stroke  = 1,fill = 0) # Realizar  cuadrado (0 sin relleno sin trazo, 1 con)
doc.roundRect(530,86,14,14,1)
doc.drawString(32,30,"NOMBRE (name)                                  FIRMA(signature):                                 FECHA-(date)")
doc.drawString(32,20, nombre )
doc.drawString(350,20, fechahoy)
doc.setFont('Helvetica',8)
doc.drawString(45,100, '     Bolilla (Ball)                           carga(charge)                                                       Bolilla(Ball)                  carga(charge)')
doc.line(30,89,158,89)
doc.line(30,71,94,71)
doc.line(30,53,200,53)
#-----------------LINEAS VERTICUALES---------------------------------

#        x   y   x  y 
doc.line(30,790,30,755)#lineas verticales encontra
doc.line(30,730,30,600)
doc.line(30,590,30,120) 
#---------------------------------------------------
doc.line(320,750,320,730) #linea vertical reporte
#---------------------------------------------------
doc.line(100,790,100,755) #2da linea verticales 
#---------------------------------------------------
doc.line(250,730,250,600) #1 linea cuadro 1
doc.line(400,730,400,600) #2 linea cuadro 1
doc.line(535,730,535,600) #3 linea cuadro 1
#--------------------------------------------------
doc.line(100,590,100,120) #1 linea cuadro 2 
doc.line(170,590,170,133) #2 linea cuadro 2
doc.line(120,502,120,370) # linea cuadro 2 quimicos
doc.line(535,590,535,370) # linea penultima cuadro 2
doc.line(535,350,535,133) # continuancion penultima cuadro 2
doc.line(520,590,520,370) # linea antepenultima cuadro 2
doc.line(520,350,520,133) # linea antepenulstima continuacion cuadro 2
#--------------------------------------------------------
#Estructura
doc.line(243,350,243,133) # primer columna
doc.line(316,350,316,120)
doc.line(389,350,389,120)
doc.line(462,350,462,133)
#---------------RESULTADO DE ENSAYO----------
doc.line(240,569,240,546)
doc.line(310,569,310,546)
doc.line(380,569,380,546)
doc.line(450,569,450,546)
doc.line(240,530,240,502)
doc.line(310,530,310,502)
doc.line(380,530,380,502)
doc.line(450,530,450,502)
#----------------QUIMICO
doc.line(50,502,50,480)
doc.line(50,370,50,350)
doc.line(50,205,50,180)
#---------------------------------------------------
doc.line(550,790,550,755)#lineas finales
doc.line(550,750,550,600)#lineas finales
doc.line(550,590,550,120)#lineas finales
#--------------------------------------------------
doc.line(30,40,30,10)
doc.line(550,40,550,10)
doc.line(170,40,170,10)
doc.line(310,40,310,10)




#------------------HORIZONTALES-----------------------
#---------ENCABEZADO-------------
doc.line(30,790,550,790) #1 encabezado
doc.line(30,755,550,755) #2 encabezado
#--------------------------------------
doc.line(320,750,550,750) # cuadro 1 superior reporte
#----------------CUADRO 1------------------------------------
doc.line(30,730,550,730) #1, cuadro 1
doc.line(30,693,550,693) #2, cuadro 1
doc.line(30,650,550,650) #3, cuadro 1
doc.line(30,600,550,600) #ultima, cuadro 1
#-------------CUADRO 2-------------------------
doc.line(30,590,550,590) #1, cuadro 2
doc.line(30,502,550,502) #2, cuadro 2 (general, tipo de ensayo inferior)
#--------------RESULTADO DEL ENSAYO---------------------------------------------------------
doc.line(170,569,520,569)
doc.line(170,546,520,546)
doc.line(170,530,520,530)

#--------------------------------------------------------------------------------
doc.line(30,480,170,480) # linea quimico)
doc.line(520,480,550,480)
doc.line(100,464,170,464) # linea si
doc.line(520,464,550,464)
doc.line(100,448,170,448) # lunea Mn
doc.line(520,448,550,448)
doc.line(100,432,170,432) # linea cr
doc.line(520,432,550,432)
doc.line(100,417,170,417) # linea Ni
doc.line(520,417,550,417)
doc.line(100,401,170,401) # linea cu
doc.line(520,401,550,401)
doc.line(100,386,170,386) # linea p
doc.line(520,386,550,386)
doc.line(30,370,550,370) #3, cuadro 2 (general, quimico inferior)
#--------------------------------------------------------------------
doc.line(30,350,550,350) #4, cuadro 2 (general, estructura inferior)
doc.line(30,330,550,330) #5, cuadro 2 (general, grafito % inferior)

#-------------------------------------------------------------------
#B C D E 
doc.line(100,310,550,310) # linea B inferior
doc.line(100,290,550,290) # linea C inferior
doc.line(100,270,550,270) # linea D inferior
doc.line(30,250,550,250) #6, cuadro 2 (general,  A B C D E inferior)
doc.line(30,230,550,230) #7, cuadro 2 (general)
doc.line(30,205,550,205) #8, cuador 2 (general)
doc.line(30,180,550,180) #9, cuadro 2 (general)

#-------------------------------------------------------
#dureza y 120 to 160
#doc.line(100,165,550,165) # min
doc.line(100,158,550,158) # max
doc.line(100,133,550,133) #penultima, cuadro 2 
doc.line(30,120,550,120) #ultima, cuadro 2
#--------------------------------------
doc.line(30,40,550,40)#penultima
doc.line(30,10,550,10) #ultima


#------------------------------ escribir-------------------
doc.showPage() #3er Pagina
doc.drawImage("NIR-0.jpg",5,50, width=600, height=750) #pegado del logo

doc.save() # Guarda y crea


