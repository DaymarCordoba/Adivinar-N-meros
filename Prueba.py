
class nodo:

	# __init__ es el constructor de la clase
	def __init__(self, dato, sig = None):
			self.dato = dato
			self.sig = sig
#fin clase

def imprimir_nodos(nodo):
	while nodo != None:
	print(nodo.dato)
	nodo = nodo.sig

#fin funcion



#Ejemplo, creamos 3 nodos 
nodo1 = nodo(1)
nodo2 = nodo(2)
nodo3 = nodo(3)

#conectamos los nodos nodo1 -> nodo2 -> nodo3 -> None/Null
nodo1.sig = nodo2
nodo2.sig = nodo3


imprimir_nodos(nodo1)
