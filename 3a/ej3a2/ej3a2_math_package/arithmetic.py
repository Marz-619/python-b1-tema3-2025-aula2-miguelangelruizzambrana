# arithmetic.py
import math

def power(base: float, exponent: float) -> float:
	return math.pow(base,exponent)

def square_root(num_1: float) -> float:
	if num_1<0:
		raise ValueError("Número negativo, no se puede calcular la raíz")
	else:
	 return math.sqrt(num_1)
	



