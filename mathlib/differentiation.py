if __package__:
    from .functions import Sym
else:
    from functions import Sym

def derivate(func, x):
    #Paso de h
    h = 1e-3
    #Decimales a redondear
    decimals=10
    #Evalucacion de las 4 funciones
    funcFoward1 = func.eva(x + h)
    funcFoward2 = func.eva(x + h*2)
    funcBackward1 = func.eva(x - h)
    funcBackward2 = func.eva(x - h*2)

    #Calculo de la derivada usando la formula de 5 puntos de cuarto orden
    result = (-funcFoward2 + 8*funcFoward1 - 8*funcBackward1 + funcBackward2) / (12 * h)
    #redondeo del resultado si se especifica el numero de decimales
    return round(result, decimals) if decimals is not None else result
