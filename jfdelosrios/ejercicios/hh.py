from sympy import *


def prueba():
  x = symbols('beta_1')
  a = Integral(cos(x)*exp(x), x)
  return('$$' + latex(a) + '$$')
