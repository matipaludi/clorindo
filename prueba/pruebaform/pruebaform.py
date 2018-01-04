#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("pruebaform.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	def _init_(self, parent=None):
		QtGui.QMainWindow._init_(self, parent)
		self.setupUi(self)
		self.btn_generar.clicked.conect(self.btn.generar_clicked)
	def btn_generar_clicked(self):
		embarque = float(self.textembarque.text())
		mini = embarque / 2
		self.text_A.setValue(int(mini))


app= QtGui.QApplication(sys.argv)
MyWindow=MyWindowClass(None)
MyWindow.show()
app.exec_()
