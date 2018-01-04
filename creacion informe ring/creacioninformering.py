import time
import os
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
cliente = 'Federal Mogul USA' #ver
dia = time.strftime("%d/%m/%y")
reporte = time.strftime("%d%m%y")

#---contador---
with open("contador.json") as g:
	c = json.load(g)
fecha= c[0]# fecha del json
contador = c[1]
fecha= fecha['fecha']
contador = int(contador['contador'])
if fecha == dia: #dia actual
	contador += 1

else:
	contador = 1
	fecha = dia
data = ({"fecha" : fecha}, {"contador" : contador})
with open ("contador.json", 'w') as f: #w de write, r de read
	json.dump(data, f)	


lotbatch = 659 #ver
reporte = reporte + '-' + str(contador)
ring = 'AR82190AV1' #ver
sampleQ= 1 #ver
Scmin= raw_input('ingrese el valor de SC minimo:  ')
Scmax= raw_input('ingrese el valor de SC maximo:  ') #mantener por ahora
doc = canvas.Canvas("reportedering.pdf", pagesize =A4)
doc.drawImage("logo.jpg",5,790, width=100, height=50) #pegado del logo
doc.drawString(10,770 , "From: Clorindo Appo S.R.L              To: " +cliente ) #pegado del cliente
doc.drawString(10, 750, "Title: Ring  " + str(ring) +    '                  Report N: ' + str(reporte) +  '                                          Date: ' + dia ) 

doc.drawString(203, 730,  "Authors: Fernando Ferrari                                Departament: Foundry")
doc.drawString(203, 710, "Lot/batch: " + str(lotbatch) + "                                                   Sample Quantity: " + str(sampleQ)  ) #ver 

doc.line(10,749,36,749)

doc.setFont("Helvetica-Bold", 12)#En negrita

doc.drawString (530, 815, "1-4")#NUMERO DE PAGINA
doc.drawString (10, 650, "Summary:")
doc.drawString (50, 630, "1- Chemical Coposition")
doc.drawString (50, 610, "2- Degree of Saturation")
doc.drawString (50, 590, "3- Tensile Stregth")
doc.drawString (50, 570, "4- Hardness")
doc.drawString (50, 550, "5- Thermal Expansion Coefficient")
doc.drawString (50, 530, "6- Microstructure")
doc.line(10,649,68,649)



doc.showPage()
doc.drawImage("logo.jpg",5,790, width=100, height=50) 
doc.drawString (530, 815, "2-4")#NUMERO DE PAGINA
doc.setFont("Helvetica-Bold", 12)
doc.drawString (10, 750, "1- Chemical Coposition:")
doc.drawString (10, 600, "2- Degree of Saturation:")
doc.drawString (10, 450, "3- Tensile Stregth:")
doc.drawString (10, 300, "4- Hardness:")
doc.drawString (10, 150, "5- Thermal Expansion Coefficient:")

doc.line(10,749,147,749) # subraya
doc.line(10,599,144,599)
doc.line(10,449,114,449)
doc.line(10,299,82,299)
doc.line(10,149,204,149)

doc.setFont("Helvetica", 12) #fuente comun
doc.drawString (150, 750, " Spectrometer Chemical Analysis is attached")
doc.drawString (148, 600, "Sc:" + str(Scmax) + ' - ' + str(Scmin) + 'O.K. (0,80 - 0,95)')
doc.drawString (118, 450, "198Mpa (n/mm2) O.k. (160-206N/mm2)")
doc.drawString (85, 300, "  125 - 137 HB (187,5 kg. - 2,5mm)        70-75RB(100kg.-1/16'') ")      
doc.drawString (85, 285, "  O.K. (120-160 HB)")
doc.drawString (208, 150, "19,2(1/ C x 10-6) O.K. (18,5 - 19,5, 20 to 400 C)")

doc.drawString (113, 200, "")
doc.showPage()
doc.drawString (530, 815, "3-4")#NUMERO DE PAGINA
doc.setFont("Helvetica-Bold", 12)
doc.drawString (50, 720, "6- Microstructure:")
doc.line(50,719,150,719)

#grafico 1
doc.drawString (50, 700, "X 100")
doc.line(50,699,548,699)#lineas horizontales
doc.line(50,533,548,533)
doc.line(50,450,548,450)
doc.line(50,699,50,450)# lineas verticales
doc.line(216,699,216,450) 
doc.line(382,699,382,450)
doc.line(548,699,548,450)
doc.drawImage("logo.jpg",10,780, width=100, height=50)#logo
doc.drawImage("foto1.bmp",52,535, width=160, height=160)#foto1
doc.drawImage("foto2.bmp",218,535, width=160, height=160)#foto2
doc.drawImage("foto3.bmp",384,535, width=160, height=160)#foto3
doc.setFont("Helvetica-Bold",12) #letra negrita
doc.drawString (52, 523, " O.D. Zone:") #titulos primer grafico
doc.drawString (218, 523, '  Middle Zone:')
doc.drawString (384,523, 'L.D. Zone:')
doc.line (54,522,116,522) # subrayado titulos 
doc.line (224,522,298,522)
doc.line (384,522,443,522)
doc.drawString (52, 509, 'Graphite tipe A 70%+B') # primer cuadro
doc.drawString (52, 495, '20%+E 10%, size 6')
doc.drawString (52, 481, 'ASTM.   O.K.')
doc.drawString (226, 509, 'Graphite tipe A 80% + B')#2do cuadro
doc.drawString (226, 495, '10%+E 10%, size 5-6')
doc.drawString (226, 481, 'ASTM.   O.K.')
doc.drawString (384, 509, 'Graphite tipe A 85%+B')#3er cuadro
doc.drawString (384, 495, '10 +E 5%, size 5-6')
doc.drawString (384, 481, 'ASTM.   O.K.')

#        x1 y1   x2  y2
#grafico 2
doc.drawString (50, 351, "X 500 Marble Etched")
doc.line(50,350,548,350)
doc.line(50,184,548,184)
doc.line(50,104,548,104)
doc.line(50,350,50,104)#VERTICALES
doc.line(216,350,216,104)
doc.line(382,350,382,104)
doc.line(548,350,548,104)
doc.drawImage("foto4.bmp",52,186, width=160, height=160)#foto4
doc.drawImage("foto5.bmp",218,186, width=160, height=160)#foto5
doc.drawImage("foto6.bmp",384,186, width=160, height=160)#foto6

doc.drawString (52, 174, " O.D. Zone:") # Titulo segundo grafico
doc.drawString (218, 174, '  Middle Zone:')
doc.drawString (384,174, 'L.D. Zone:')
doc.line (54,173,116,173)
doc.line (224,173,298,173)
doc.line (384,173,443,173)
doc.drawString (54,153, 'Carbides Level: 2 to 3')
doc.drawString (54,138, '% O.K.')
doc.drawString (220,153, 'Carbides Level: 2 to 3')
doc.drawString (220,138, '% O.K.')
doc.drawString (384,153, 'Carbides Level: 2 to 3')
doc.drawString (384,138, '% O.K.')

doc.drawString (50,60,'Controlled:') #Firma
doc.line (50,59,112,59)

doc.showPage() #3er Pagina
doc.drawImage("NIR-0.jpg",5,50, width=600, height=750) #pegado del logo
#doc.drawImage("NIR-1.jpg",5,20, width=600, height=200) #pegado del logo


doc.save()
print 'guardado'
