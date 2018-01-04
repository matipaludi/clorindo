#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Convierte temperaturas
# www.pythondiario.com
 
import sys
from PyQt4 import QtCore, QtGui, uic
import datetime
import time
# Cargar nuestro archivo .ui
form_class = uic.loadUiType("informeCalidad.ui")[0]
#union con elementos del .ui y eventos particulares
class MyWindowClass(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		fecha= datetime.date.today()
		self.date_Fecha.setDate(fecha)
		self.btn_generar.clicked.connect(self.btn_generar_clicked)
		self.btn_exit.clicked.connect(self.btn_exit_clicked)
		self.btn_borrar.clicked.connect(self.btn_borrar_clicked)
		self.edit_embarque.setFocus()		
		#print dir(self.date_Fecha)	
		 # Evento del boton Gnerar
	def btn_generar_clicked(self):				
		embarque = self.edit_embarque.text()
		embarque = str(embarque)		
		if embarque.isdigit():# si embarque tiene letras
			print 'a'		
		if self.spin_muestras.value() > 1:	# si hay mas de una muestra dar la posibilidad de ingreasar mas de una
			fechacoladam = str(self.date_Fecha.text())
			turnom = str(self.edit_turno.text())
			Am = str(self.edit_A.text())
			Bm = str(self.edit_B.text())
			Dm = str(self.edit_D.text())
			Em = str(self.edit_E.text())
			cantidadm = str(self.edit_cantidad.text())
			minimom = str(self.edit_min.text())
			maximom = str(self.edit_max.text())
			#terminada la primer muestra borro todo y hago foco correspondiente
			self.date_Fecha.setFocus()

			self.edit_turno.setText('')
			self.edit_A.setText('')
			self.edit_B.setText('')
			self.edit_D.setText('')
			self.edit_E.setText('')
			self.edit_cantidad.setText('')
			self.edit_min.setText('')
			self.edit_max.setText('')
			fecha= datetime.date.today()			
			self.date_Fecha.setDate(fecha)
			turno = self.edit_turno.text()
			turno = str(turno)
			turno = turno.upper()
		if turno.lsdigit() == False:
			print 'a'
			#si el turno tiene un numero
		self.edit_turno.setText(turno)
				
		if self.m_embarque.isChecked():
			print 'hola'
		if self.m_PPAP.isChecked():
			print 'hola2'			
	def btn_borrar_clicked(self):
		self.edit_embarque.setText('')
		self.edit_turno.setText('')
		self.edit_A.setText('')
		self.edit_B.setText('')
		self.edit_D.setText('')
		self.edit_E.setText('')
		self.edit_cantidad.setText('')
		self.edit_min.setText('')
		self.edit_max.setText('')
		self.edit_nombre.setText('')
		self.date_Fecha.setDate(fecha)
	def btn_exit_clicked(self):
		exit()
	 
'''
 def btn_MainWindow_show(self):
	fechahoy = time.strftime("%d/%m/%y")
	self.date_Fecha.setvalue = fechahoy
 # Evento del boton btn_FtoC
 def btn_FtoC_clicked(self):
  fahr = self.spinFahr.value()
  cel = ((fahr - 32) * 5) / 9
  self.edit_embarque.setText(str(cel))
 '''
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()
