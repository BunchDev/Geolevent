# -*- coding: utf-8 -*-

#######################################################
# Organizacion : BUNCHDEV 							  #
# Autores: 											  #
# - Cristian Michel Perez Zarate					  #
# - Edy Cristhian Gomez Vasquez						  #
# - Cesar Alejandro Berdejo Rincon					  #
# - Alexis Tadeo Hernandez							  #
# Fecha: 26 - Diciembre - 2015						  #
# 			Todos los derechos reservados			  #	
#######################################################

import flask
import json

"""
La clase JsonProceso se encarga de recibir y procesar los datos requeridos y transformarlos en formato JSON
"""


class JsonProceso:
	#se declaran todos los atributos que forman parte de la clase
	def __init__(self):
		jsonLocal = ""
	#-------------procesarPeticion----------------------
	#Este metodo lee correctamente el encabezado del Json y en base a eso realiza una accion
	def procesarPeticion(self,jsonInput):
		self.jsonLocal = json.loads(jsonInput)
		


