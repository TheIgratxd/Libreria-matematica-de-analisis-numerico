from mathlib import Sym, derivate

x = Sym("x")

func = x**2

print("Function: ", func.eva(3))
print("Derivative: ", derivate(func, 3))