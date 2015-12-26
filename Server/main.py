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
from jsonProcesos import * 

"""
Script main.py contiene todos los metodos y objetos principales que el servidor ejecuta
asi como tambien llamadas a librerias externas.
"""
#############
# Variables #
#############





##############
# Constantes #
##############











def main():
	jsonProc = JsonProceso()
	jsonTest = ' {"eventos" : [ {"cabecera": "request-events","longitud": -1234.4544, "latitud": -234.6776   },{"cabecera": "request-events","longitud": -1234.4544, "latitud": -234.6776   },{"cabecera": "request-events","longitud": -1234.444, "latitud": -23.6776   },{"cabecera": "request-events","longitud": -1234.4546, "latitud": -234.6766   } ] }'
	jsonProc.procesarPeticion(jsonTest)












if __name__ == "__main__":
	main()