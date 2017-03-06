#!/usr/bin/env python
# -*- coding : utf-8 -*-
from flask import Flask, request, Response
app = Flask("EDD")

class _Nodo():
	"""docstring for ClassName"""
	def __init__(self, dato):
		self.siguiente = None
		self.indice = None
		self.palabra = dato
	
	def __str__(self):
			return str(self.palabra)	

class Lista1():
	"""docstring for Lista1"""
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.contador = 0

	def vacia(self):
		if (self.primero == None):
			return True
		else:
			return False

	def agregarFinal(self, palabra):	#No valido si el dato ya existe
		nuevo = _Nodo(palabra)
		if self.primero==None:
			nuevo.indice = self.contador
			self.ultimo = nuevo
			self.primero = self.ultimo 				
		else:
			self.contador = self.contador + 1
			nuevo.indice = self.contador
			self.ultimo.siguiente = nuevo
			self.ultimo = nuevo
		nuevaLista.mostrarElemento()
		return "agregado: " + palabra
		
	def buscar(self, palabra):			
		actual = self.primero
		indice = 0
		if self.primero==None:
			return "No hay datos en la lista"
		while actual!= None:
			if actual.palabra==palabra:
				x = str(actual.indice)
				indice = 'El dato se encuentra en el indice: '+  x
				break
			else:
				indice = 'No se encontro el dato'
			actual = actual.siguiente
		return indice

	def eliminar(self, indice):
		indice1 = int(indice)
		actual = self.primero
		if (self.primero==None):
			return "No hay datos en la lista"
		elif (self.primero.siguiente==None and self.primero.indice == indice1):
			self.primero = None 
			self.ultimo = None
			self.contador = 0
			nuevaLista.mostrarElemento()
			return "Indice eliminado, No existen nodos"
		elif self.primero.indice==indice1:
			self.primero = self.primero.siguiente
			self.contador = self.contador - 1
			nuevaLista.actualizarIndice()
			nuevaLista.mostrarElemento()
			return "Indice eliminado"
		else:
			anterior = actual
			actual = actual.siguiente
			indice2 = 0			
			while actual!= None:
				if actual.indice==indice1:
					anterior.siguiente = actual.siguiente
					self.contador = self.contador - 1
					nuevaLista.actualizarIndice()
					nuevaLista.mostrarElemento()
					return "Nodo Eliminado"

				else:
					indice2 = 'No se encontro el dato'
				anterior = actual
				actual = actual.siguiente
			return "No se encontro el dato"

	def mostrarElemento(self):					
		with open('C:\\txt\\lista.txt','w') as file:
			file.write('Digraph g{\n\n')
			if (self.vacia==True):			
				file.write('Lista vacia\n\n')
			else:
				actual = self.primero
				while actual != None:
					if actual.siguiente!=None:					
						file.write(actual.palabra + ' -> ' + actual.siguiente.palabra+'\n')
					elif actual.siguiente==None and self.contador < 1:
						file.write(actual.palabra +'\n')						
					actual = actual.siguiente
			file.write('\n}')
		file.close()

	def actualizarIndice(self):
		actual = self.primero
		temp = 0
		while actual!=None:
			actual.indice = temp
			temp = temp + 1
			actual = actual.siguiente

#--------------------------------------------------------------------^LISTA^---------------------------------------------------------------------

class _NodoCola():
	"""docstring for ClassName"""
	def __init__(self, numero):
		self.numero = numero
		self. siguiente = None

class Cola():
	"""docstring for Cola"""
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		if (self.primero == None):
			return True
		else:
			return False

	def agregarFinal(self, numero):	#No valido que el dato no exista y tampoco que solo sea numero
		nuevo = _NodoCola(numero)
		if self.primero==None:
			self.ultimo = nuevo
			self.primero = self.ultimo
			with open('C:\\txt\\cola.txt','w') as file:
				file.write('Digraph g{\n\n')
				file.write(numero)
				file.write('\n\n}')
			file.close()
			return "agregado: " + numero
		else:
			self.ultimo.siguiente = nuevo
			self.ultimo = nuevo
			nuevaCola.mostrarElemento()
		return "agregado: " + numero

	def sacarInicio(self):
		if self.primero==None:
			return "No hay datos en la cola"
		elif self.primero.siguiente==None:
			temp = self.primero.numero
			self.primero = None
			self.ultimo = None
			nuevaCola.mostrarElemento()
			return "Se saco de la cola: " + temp + ", No hay mas datos"
		else: 
			temp = self.primero.numero
			self.primero = self.primero.siguiente
			nuevaCola.mostrarElemento()
			return "Se saco de la cola: " + temp

	def mostrarElemento(self):					
		with open('C:\\txt\\cola.txt','w') as file:
			file.write('Digraph g{\n\n')
			if (self.vacia==True):			
				file.write('Cola vacia\n\n')
			elif self.primero!=None and self.primero.siguiente==None :
				file.write(self.primero.numero)
			else:
				actual = self.primero
				while actual != None:
					if actual.siguiente!=None:					
						file.write(actual.numero + ' -> ' + actual.siguiente.numero+'\n')											
					actual = actual.siguiente
			file.write('\n}')
		file.close()

#------------------------------------------------------------------------^COLA^-------------------------------------------------------------------

class _NodoPila():
	"""docstring for ClassName"""
	def __init__(self, numero):
		self.numero = numero
		self. siguiente = None

class Pila():
	"""docstring for Cola"""
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		if (self.primero == None):
			return True
		else:
			return False

	def agregarFinal(self, numero):	#No valido que el dato no exista y tampoco que solo sea numero
		nuevo = _NodoPila(numero)
		if self.primero==None:
			self.ultimo = nuevo
			self.primero = self.ultimo
			with open('C:\\txt\\pila.txt','w') as file:
				file.write('Digraph g{\n\n')
				file.write(numero)
				file.write('\n\n}')
			file.close()
			return "agregado: " + numero
		else:
			self.ultimo.siguiente = nuevo
			self.ultimo = nuevo
			nuevaPila.mostrarElemento()
		return "agregado: " + numero

	def sacarPila(self):
		if self.ultimo==None:
			return "No hay datos en la pila"
		elif self.primero.siguiente==None:
			temp = self.primero.numero
			self.primero = None
			self.ultimo = None
			nuevaPila.mostrarElemento()
			return "Se saco de la pila: " + temp + ", No hay mas datos"
		else: 
			temp = self.ultimo.numero
			actual = self.primero
			while actual.siguiente!=None and actual.siguiente!=self.ultimo:
				actual = actual.siguiente
			actual.siguiente = None	
			self.ultimo = actual
			nuevaPila.mostrarElemento()
			return "Se saco de la pila: " + temp

	def mostrarElemento(self):					
		with open('C:\\txt\\pila.txt','w') as file:
			file.write('Digraph g{\n\n')
			if (self.vacia==True):			
				file.write('Pila vacia\n\n')
			elif self.primero!=None and self.primero.siguiente==None :
				file.write(self.primero.numero)
			else:
				actual = self.primero
				while actual != None:
					if actual.siguiente!=None:					
						file.write(actual.numero + ' -> ' + actual.siguiente.numero+'\n')											
					actual = actual.siguiente
			file.write('\n}')
		file.close()


#------------------------------------------------------------------------^PILA^-------------------------------------------------------------------

class _NodoMatriz(object):
	
	def __init__(self):
		self.arriba = None
		self.abajo = None
		self.izq = None
		self.der = None
		self.frente = None
		self.atras = None
		# valores de encabezado
		self.letra = None
		self.dominio = None
		#valores de nodo
		self.columna = 1
		self.nombre = ""

class Matriz():
	
	def __init__(self):
		# indican el inicio de la matriz
		self.IndiceCol = None # nodo que representa la fila de encabezados de columna
		self.IndiceFil= None  # nodo que representa la columna de encabezados de fila
		#self.contadorColumna = 1

	def agregarCorreo(self, letra, nombre, dominio):
		if self.IndiceFil==None and self.IndiceCol==None: # si la matriz esta vacia
			# se crea dos nodos indices: letra y dominio y un nodo para el nombre
			nuevoIndiceFil = _NodoMatriz()
			nuevoIndiceCol = _NodoMatriz()
			nuevoNodo = _NodoMatriz()
			# agrego a la matriz
			self.IndiceFil = nuevoIndiceFil
			self.IndiceCol = nuevoIndiceCol
			# valores de encabezados 
			nuevoIndiceFil.letra = letra
			nuevoIndiceCol.dominio = dominio
			# atributos de nodo
			nuevoNodo.dominio = dominio
			nuevoNodo.nombre = nombre
			# conexiones de nodo
			nuevoNodo.izq = self.IndiceFil
			nuevoNodo.arriba = self.IndiceCol
			# conexiones de encabezados
			nuevoIndiceFil.der = nuevoNodo
			nuevoIndiceCol.abajo = nuevoNodo
			self.recorrerMatriz()
			return "agregarCorreo indices == None"
		else:
			posicionFila = self.ObtenerIndiceFila(letra)
			posicionCol = self.ObtenerIndiceColumna(dominio)

			if posicionFila!="error" and posicionCol!="error":
				nodoColumna = self.agregarNodoColumna(posicionCol,nombre,dominio)
				if nodoColumna!="atras":
					nodoFila = self.agregarNodoFila(posicionFila,nodoColumna,dominio)
					return nodoFila
				return nodoColumna
			else: 
				return posicionFila
			return posicionFila

	def ObtenerIndiceFila(self, letra):# devuelve el nodoIndice Fila donde se va a ingresar el dato
		actual = self.IndiceFil
		while actual!=None:			
			if actual.letra == letra: 	# la letra existe
				return actual
			elif actual.letra>letra: 	# la letra no existe
				if actual.arriba ==None:
					"""se anade a la primera posicion"""
					nuevo = _NodoMatriz()
					nuevo.letra = letra
					nuevo.abajo = actual
					actual.arriba = nuevo
					self.IndiceFil = nuevo
					return nuevo
				else:					# se anade en medio de dos nodos
					nuevo = _NodoMatriz()
					nuevo.letra = letra
					actual.arriba.abajo = nuevo
					nuevo.arriba = actual.arriba
					nuevo.abajo = actual
					actual.arriba = nuevo
					return nuevo
			elif actual.abajo == None: 	# se anade un nodo al final porque no existe letra y no es menor a las anteriores
				nuevo = _NodoMatriz()
				nuevo.letra = letra
				actual.abajo = nuevo
				nuevo.arriba = actual
				return nuevo
			# sumar al contador de fila
			actual = actual.abajo 
		return "error"

	def ObtenerIndiceColumna(self, dominio):# devuelve el nodoIndice Columna donde se va a ingresar el dato
		actual = self.IndiceCol
		while actual!=None:	
			if actual.dominio==dominio:		#el dominio existe
				return actual
			elif actual.dominio > dominio:	#el dominio no existe
				if actual.izq==None:		# se anade a la primera posicion
					nuevo = _NodoMatriz()
					nuevo.dominio = dominio
					nuevo.der = actual
					actual.izq = nuevo
					self.IndiceCol = nuevo
					return nuevo
				else:						# se anade en medio de dos nodos
					nuevo = _NodoMatriz()
					nuevo.dominio = dominio
					actual.izq.der = nuevo
					nuevo.izq = actual.izq
					nuevo.der = actual
					actual.izq = nuevo
					return nuevo
			elif actual.der==None :			# se anade un nodo al final porque el dominio no existe y no es menor a las anteriores
				nuevo = _NodoMatriz()
				nuevo.dominio = dominio
				actual.der = nuevo
				nuevo.izq = actual
				return nuevo
			actual = actual.der
		return "error"

#-----------------------------------------------------------------------------------------------------------------------------Metodos al reves para agregar el nodo
	def agregarNodoColumna(self, nodo, nombre, dominio):		#anade el nodo en la columna que le corresponde, nodoIndice, nombre del correo, dominio del correo
		if nodo.abajo==None:						# si el indice columna no tiene nodos
			nuevo = _NodoMatriz()
			# anade atributos al nodo
			nuevo.dominio = dominio
			nuevo.nombre = nombre
			# enlazar nodo con indice de columna
			nodo.abajo = nuevo
			nuevo.arriba = nodo
			#self.recorrerMatriz()
			return nuevo
		else:
			actual = nodo.abajo
			while actual!=None:
				if actual.nombre[0]==nombre[0]:	# el nodo existe, ingresar nodo detras ------------------- retornar None porque no se va a enlazar con filas
					if actual.atras==None:		# si no hay nada atras del dodo
						nuevo = _NodoMatriz()
						nuevo.dominio = dominio
						nuevo.nombre = nombre
						actual.atras = nuevo
						nuevo.frente = actual
						self.recorrerMatriz()
						return "atras"
					else:						# agrega el nuevo nodo hasta de ultimo en los atras
						while actual.atras!=None:
							actual = actual.atras
						nuevo = _NodoMatriz()
						nuevo.dominio = dominio
						nuevo.nombre = nombre
						actual.atras = nuevo
						nuevo.frente = actual
						self.recorrerMatriz()
						return "atras"
				elif actual.nombre[0]>nombre[0]:	# el nodo no existe, se ingresa en medio de dos nodos
					nuevo = _NodoMatriz()
					nuevo.nombre = nombre
					nuevo.dominio = dominio
					actual.arriba.abajo = nuevo
					nuevo.arriba = actual.arriba
					nuevo.abajo = actual
					actual.arriba = nuevo
					#self.recorrerMatriz()
					return nuevo
				elif actual.abajo == None:			# el nodo no existe y no es menor a las anteriores
					nuevo = _NodoMatriz()
					nuevo.dominio = dominio
					nuevo.nombre = nombre
					actual.abajo = nuevo
					nuevo.arriba = actual
					#self.recorrerMatriz()
					return nuevo
				actual = actual.abajo
			return "agregarNodoColumna, no agregado"

	def agregarNodoFila(self,indiceFila, nodo, dominio):
		if indiceFila.der==None:	# el indice no contiene enlaces 
			indiceFila.der = nodo
			nodo.izq = indiceFila
			self.recorrerMatriz()
			return "agregarNodoFila ==, agregado" 
		else:						# el indice contiene por lo menos un nodo
			actual = indiceFila.der			
			while actual!=None:
				if actual.dominio>dominio:
					actual.izq.der = nodo
					nodo.der = actual
					nodo.izq = actual.izq
					actual.izq = nodo
					self.recorrerMatriz()
					return "agregarNodoFila >, agregado"
				elif actual.der==None:
					actual.der = nodo
					nodo.izq = actual
					self.recorrerMatriz()
					return "agregarNodoFila == None"
				actual = actual.der
			return "agregarNodoFila, No agregado"

	def recorrerLetra(self, letra):
		actual = self.IndiceFil
		while actual!=None:			
			if actual.letra == letra: 	# la letra existe
				break
			elif actual.abajo==None:
				actual = None
			actual = actual.abajo
		if actual!=None:
			with open('C:\\txt\\Letra.txt','w') as file:
				file.write('Digraph g{\n\n')
				file.write(actual.letra+' -> '+ actual.der.nombre+'\n\n')
				file.write(actual.der.nombre+' -> '+ actual.letra+'\n\n')
				actual = actual.der
				while actual!=None:
				 	temp = actual
				 	if actual.atras!=None:
				 	 	while temp!=None:
				 	 		if temp.atras!=None:
				 	 			file.write(temp.nombre+' -> '+temp.atras.nombre+'\n\n')
				 	 			file.write(temp.atras.nombre+' -> '+temp.nombre+'\n\n')
				 	 		temp = temp.atras				 	
				 	if actual.der!=None:
				 	 	file.write(actual.nombre+' -> '+actual.der.nombre+'\n\n')
				 	 	file.write(actual.der.nombre+' -> '+actual.nombre+'\n\n')
				 	actual = actual.der
				file.write('}\n\n')
			file.close()
			return "lista generada letras"
		return "no se encuentra la letra"

	def recorrerDominio(self, dominio):
		actual = self.IndiceCol
		while actual!=None:			
			if actual.dominio == dominio: 	# la letra existe
				break
			elif actual.der==None:
				actual = None
			actual = actual.der
		if actual!=None:
			with open('C:\\txt\\Dominio.txt','w') as file:
				file.write('Digraph g{\n\n')
				file.write(actual.dominio+' -> '+ actual.abajo.nombre+'\n\n')
				file.write(actual.abajo.nombre+' -> '+ actual.dominio+'\n\n')
				actual = actual.abajo
				while actual!=None:
				 	temp = actual
				 	if actual.atras!=None:
				 	 	while temp!=None:
				 	 		if temp.atras!=None:
				 	 			file.write(temp.nombre+' -> '+temp.atras.nombre+'\n\n')
				 	 			file.write(temp.atras.nombre+' -> '+temp.nombre+'\n\n')
				 	 		temp = temp.atras				 	
				 	if actual.abajo!=None:
				 	 	file.write(actual.nombre+' -> '+actual.abajo.nombre+'\n\n')
				 	 	file.write(actual.abajo.nombre+' -> '+actual.nombre+'\n\n')
				 	actual = actual.abajo
				file.write('}\n\n')
			file.close()
			return "lista generada dominios"
		return "no se encuentra el dominio"

	def recorrerMatriz(self):
		with open('C:\\txt\\Matriz.txt','w') as file:
			file.write('Digraph g{\n\n')
			file.write('graph[center=1 ,rankdir=LR];\n\n')
			actualIndiceColumna = self.IndiceCol
			#recorrido columna, y atras
			temp = self.IndiceCol
			while temp!=None:
				if temp.der!=None:
					file.write(temp.dominio+' -> '+temp.der.dominio+'\n')
					file.write(temp.der.dominio+' -> '+temp.dominio+'\n')
				temp = temp.der
			
			temp = self.IndiceFil
			while temp!=None:
				if temp.abajo!=None:
					file.write(temp.letra+' -> '+temp.abajo.letra+'\n')
					file.write(temp.abajo.letra+' -> '+temp.letra+'\n')
				temp = temp.abajo

			while actualIndiceColumna!=None:
				file.write(actualIndiceColumna.dominio + ' -> ' + actualIndiceColumna.abajo.nombre+'\n')
				file.write(actualIndiceColumna.abajo.nombre + ' -> ' + actualIndiceColumna.dominio+'\n')
				actualNodo = actualIndiceColumna.abajo
				while actualNodo!=None:
					if actualNodo.abajo!=None:
						file.write(actualNodo.nombre + ' -> ' + actualNodo.abajo.nombre+'\n')
						file.write( actualNodo.abajo.nombre + ' -> ' + actualNodo.nombre+'\n')
					actualNodo = actualNodo.abajo
				actualIndiceColumna = actualIndiceColumna.der
			# recorrido fila			
			actualIndiceFila = self.IndiceFil
			while actualIndiceFila!=None:
				file.write('subgraph cluster_'+actualIndiceFila.letra+'{\n\n')
				file.write(actualIndiceFila.letra + ' -> ' + actualIndiceFila.der.nombre+'\n')
				file.write(actualIndiceFila.der.nombre + ' -> ' + actualIndiceFila.letra+'\n')
				actualNodo = actualIndiceFila.der
				while actualNodo!=None:
					if actualNodo.der!=None:
						file.write(actualNodo.nombre + ' -> ' + actualNodo.der.nombre+'\n')
						file.write( actualNodo.der.nombre + ' -> ' + actualNodo.nombre+'\n')
					actualNodo = actualNodo.der
				actualIndiceFila = actualIndiceFila.abajo
				file.write('}\n\n')
			file.write('\n}')
		file.close()

#-------------------------------------------------------^Eliminar de la matriz^----------------------------------------
	def EliminarNodoMatriz(self, letra, nombre, dominio):
		posFila = self.obtenerFilaEliminar(letra)
		posColumna = self.obtenerColumnaEliminar(dominio)
		if posColumna!="no" and posFila!="no":
			nodoEliminar = self.obtenerNodoEliminar(posColumna,nombre,letra)
			#print nodoEliminar
			if nodoEliminar !="no" and nodoEliminar !="si":
				if nodoEliminar.atras!=None:						# elimina si el nodo es el primero y hay detras
					nuevoEnfrente = nodoEliminar.atras
					# conexiones del nodo hacia todos las direcciones	
					nuevoEnfrente.arriba = nodoEliminar.arriba
					nuevoEnfrente.abajo = nodoEliminar.abajo
					nuevoEnfrente.izq = nodoEliminar.izq
					nuevoEnfrente.der = nodoEliminar.der
					nuevoEnfrente.frente = nodoEliminar.frente
					#conexion de los nodos al rededor hacia el nuevo
					nodoEliminar.izq.der = nuevoEnfrente
					nodoEliminar.arriba.abajo = nuevoEnfrente
					if nodoEliminar.abajo!=None:
						nodoEliminar.abajo.arriba= nuevoEnfrente
					if nodoEliminar.der!=None:
						nodoEliminar.der.izq = nuevoEnfrente
					self.recorrerMatriz()
					return "eliminado frente"
				else:												# elimina otro tipo de nodo
					if nodoEliminar.abajo!=None:
						nodoEliminar.arriba.abajo = nodoEliminar.abajo
						nodoEliminar.abajo.arriba = nodoEliminar.arriba
					elif nodoEliminar.arriba.arriba!=None:	# hay un nodo a la izquierda
						nodoEliminar.arriba.abajo = None
						print "uuuu"
					else:	# no hay nodo a la izquierda, eliminar indice
						if posColumna.izq ==None:					#indice es el primero
							self.IndiceCol = posColumna.der
							self.IndiceCol.izq = None
							print "que hace"
						elif posColumna.der==None:					# indice es el ultimo
							posColumna.izq.der = None
							print "creo que es aqui"
						else:										# indice esat en medio
							posColumna.izq.der = posColumna.der
							posColumna.der.izq = posColumna.izq
							print "porque"
					#------------------------- eliminar fila					
					if nodoEliminar.der!=None:
						nodoEliminar.izq.der = nodoEliminar.der
						nodoEliminar.der.izq = nodoEliminar.izq
						self.recorrerMatriz()
						return "nodo eliminado"
					elif nodoEliminar.izq.letra==None :	# hay un nodo arriba						
						nodoEliminar.izq.der = None
						print "abc"
						self.recorrerMatriz()
						return "nodo eliminado"
					else: # no hay nodo arriba, eliminar indice
						if posFila.arriba ==None:					# indice es el primero
							self.IndiceFil = posFila.abajo
							self.IndiceFil.arriba = None
							self.recorrerMatriz()
							return "nodo eliminado"
						elif posFila.abajo==None:					# indice es el ultimo
							posFila.arriba.abajo = None
							self.recorrerMatriz()
							return "nodo eliminado"
						else:										# indice esta en medio
							posFila.arriba.abajo = posFila.abajo
							posFila.abajo.arriba = posFila.arriba
							self.recorrerMatriz()
							return "nodo eliminado"		
					self.recorrerMatriz()
					return "nodo Eliminado" 
			elif nodoEliminar == "si":
				self.recorrerMatriz()
				return "eliminado atras nodo" 
			else:
				return "No Existe1"
		else:
			return "No existe2"
		return "Accion no completada"

	def obtenerNodoEliminar(self, indiceColumna,nombre,letra): # eliminar detras aqui hacerlo hacerlo hacerlo hacerlo!
		actual = indiceColumna.abajo
		while actual!=None:
			if actual.nombre==nombre:
				#print actual.nombre
				return actual
			elif actual.nombre[0]==letra:				
				temp = actual.atras
				while temp!=None:
					if temp.nombre == nombre:
						temp.frente.atras = temp.atras
						if temp.atras!=None:
							temp.atras.frente = temp.frente
							self.recorrerMatriz()
							return "si"	
						self.recorrerMatriz()
						return "si"
					temp = temp.atras
				return "no"
			actual = actual.abajo
		return "no"

	def obtenerColumnaEliminar(self, dominio):
		actual = self.IndiceCol
		while actual!=None:
			if actual.dominio==dominio:
				return actual
			actual = actual.der
		return "no"

	def obtenerFilaEliminar(self,letra):
		actual = self.IndiceFil
		while actual!=None:
			if actual.letra==letra:
				return actual
			actual = actual.abajo
		return "no"
#------------------------------------------------------------------------^MATRIZ^------------------------------------------------------------------
nuevaPila = Pila()
nuevaLista = Lista1()
nuevaCola = Cola()
nuevaMatriz = Matriz()

@app.route('/BuscarLista',methods=['POST']) 
def BuscarLista():
	parametro = str(request.form['dato'])
	return nuevaLista.buscar(parametro)

@app.route('/AgregarLista',methods=['POST']) 
def agregarLista():
	parametro = str(request.form['dato'])
	return nuevaLista.agregarFinal(parametro)

@app.route('/EliminarLista',methods=['POST']) 
def EliminarLista():
	parametro = str(request.form['dato'])
	return nuevaLista.eliminar(parametro)

#-------------------------------------------------^WSLista^--------------------------------------------------------------------------

@app.route('/SacarCola',methods=['POST']) 
def SacarCola():
	return nuevaCola.sacarInicio()


@app.route('/MeterCola',methods=['POST']) 
def MeterCola():
	parametro = str(request.form['dato'])
	return nuevaCola.agregarFinal(parametro)
#-------------------------------------------------^WSCola^---------------------------------------------------------------------------

@app.route('/SacarPila',methods=['POST']) 
def SacarUltimo():
	return nuevaPila.sacarPila()


@app.route('/MeterPila',methods=['POST']) 
def MeterPilaFin():
	parametro = str(request.form['dato'])
	return nuevaPila.agregarFinal(parametro)

#-------------------------------------------------^WSPila^---------------------------------------------------------------------------

@app.route('/MeterMatriz',methods=['POST']) 
def MeterMatriz():
	letra = str(request.form['letra'])
	nombre = str(request.form['nombre'])
	dominio = str(request.form['dominio'])
	return nuevaMatriz.agregarCorreo(letra,nombre,dominio)

@app.route('/ObtenerLetra',methods=['POST']) 
def ObtenerLetra():
	letra = str(request.form['letra'])
	return nuevaMatriz.recorrerLetra(letra)

@app.route('/ObtenerDominio',methods=['POST']) 
def ObtenerDominio():
	dominio = str(request.form['dominio'])
	return nuevaMatriz.recorrerDominio(dominio)

@app.route('/SacarMatriz',methods=['POST']) 
def SacarMatriz():
	letra = str(request.form['letra'])
	nombre = str(request.form['nombre'])
	dominio = str(request.form['dominio'])
	return nuevaMatriz.EliminarNodoMatriz(letra,nombre,dominio)

#-------------------------------------------------^WSMatriz^---------------------------------------------------------------------------
if __name__ == "__main__":
	app.run(debug=True, host='127.0.0.1')

