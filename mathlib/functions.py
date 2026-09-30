import math
import operator

class nodo:

    def _to_node(self, valor):
        if isinstance(valor, (int, float)):
            return Const(valor)
        return valor

    #Paso 4: Llegan los parametros y dependiendo de la operacion que se quiera realizar se manda a llamar el constructor de la clase ExpBi y manda el tipo de operacion que se va a realizar
    def __add__(self, otro):
        #Paso 4.1: Si el otro parametro es un int o float, lo convierte en un objeto de la clase Const
        #Paso 4.2: Crea un objeto de la clase ExpBi con los parametros que se le pasaron y el tipo de operacion que se va a realizar
        return ExpBi(self, self._to_node(otro), operator.add)

    def __sub__(self, otro):
        return ExpBi(self, self._to_node(otro), operator.sub)

    def __mul__(self, otro):
        return ExpBi(self, self._to_node(otro), operator.mul)

    def __truediv__(self, otro):
        return ExpBi(self, self._to_node(otro), operator.truediv)

    def __pow__(self, otro):
        return ExpBi(self, self._to_node(otro), operator.pow)

    def __radd__(self, otro):
        return ExpBi(self._to_node(otro), self, operator.add)
    
    def __rsub__(self, otro):
        return ExpBi(self._to_node(otro), self, operator.sub)
    
    def __rmul__(self, otro):
        return ExpBi(self._to_node(otro), self, operator.mul)
    
    def __rtruediv__(self, otro):
        return ExpBi(self._to_node(otro), self, operator.truediv)

    def __rpow__(self, otro):
        return ExpBi(self._to_node(otro), self, operator.pow)

    #Funciones trigonometricas
    def cos(self, grados=False):
        return ExpUni(self, math.cos, grados)
    
    def sin(self, grados=False):
        return ExpUni(self, math.sin, grados)

    def tan(self, grados=False):
        return ExpUni(self, math.tan, grados)

    #Logaritmos
    def log(self, otro = math.e):
        #Logaritmo natural
        if otro == math.e:
            return ExpUni(self, math.log)
        else:
        #Logaritmo en base n
            return ExpBi(self, self._to_node(otro), math.log)

    #Exponencial
    def exp(self):
        return ExpUni(self, math.exp)

class ExpBi(nodo):
#Paso 5: Se construye el objeto de la clase ExpBi con los parametros que se le pasaron y el tipo de operacion que se va a realizar
    def __init__(self, izquierda, derecha, function):
        self.izquierda = izquierda
        self.derecha = derecha
        self.function = function

    def eva(self, value_x):
        izq = self.izquierda.eva(value_x)
        der = self.derecha.eva(value_x)

        return self.function(izq, der)

class ExpUni(nodo):
    def __init__(self, value_x, function, grados=False):
        self.value = value_x
        self.function = function
        self.grados = grados

    def eva(self, value_x):
        val = self.value.eva(value_x)

        if self.grados:
            val = math.radians(val)
        
        return self.function(val)

#Paso 2: Se crea el objeto simbolo (x)
class Sym(nodo):
    #Paso 2.1: Se guarda el parametro (x)
    def __init__(self, nombre):
        self.nombre = nombre

    def eva(self, value_x):
        return value_x
    
class Const(nodo):
    def __init__(self, valor):
        self.valor = valor

    def eva(self, value_x):
        return self.valor
