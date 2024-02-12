from sympy.printing import latex
from sympy import div, Eq, solve_undetermined_coeffs, Symbol, symbols, div
from sympy.abc import k, x
from latex2sympy2 import latex2sympy


def comprobar2a4(_dividendo:str, _divisor:str, variables:dict) -> None:
    """"""

    dividendo = latex2sympy(_dividendo)
    divisor = latex2sympy(_divisor)
    variables = [(Symbol(key), value) for key, value in variables.items()]

    residuo = div(
        dividendo.subs(variables), 
        divisor
        )[1]

    print("residuo: " + '$' + latex(residuo) + '$')
    
    
def encontrar(_dividendo:str, _divisor:str, _variables:list) -> None:
    """Busca los valores de las variables guardadas en _variables 
    para que _dividendo sea multiplo de _divisor"""

    dividendo = latex2sympy(_dividendo)
    divisor = latex2sympy(_divisor)
    variables = [Symbol(valor) for valor in _variables]

    resultado = solve_undetermined_coeffs(
            Eq(div(dividendo, divisor)[1], k * divisor), 
            variables + [k], 
            x
        )

    for variable in variables:   
        print(r'$$ \{} = {} $$'.format(variable, resultado[variable]))


def punto6(p:str, q:str, r:str, operacion:str, lis:list) -> None:
    """"""

    _x, _p, _q, _r = symbols('x, p, q, r')
    
    p = latex2sympy(p)
    q = latex2sympy(q)
    r = latex2sympy(r)
    
    operacion = latex2sympy(operacion) 

    Resultante = operacion.subs([(_p,p), (_q, q), (_r, r)]).simplify().expand().cancel()

    print(
        '$$f(x) = {} =$$\n$$={}$$\n'.format(latex(operacion), latex(Resultante))
      )
        
    _v = [
      "f({}) = {}".format(valor,latex(Resultante.subs(_x, valor))) for valor in lis
      ]
    
    print('\n\n\n$$'+' \qquad '.join(_v)+'$$')
        
        
def punto7(p_text:str, q_text:str, lis:list) -> None:
    """"""
    
    print(
        '$$f(x) = ' + r'\frac{ '+ p_text +' }{ ' +  q_text + '}' + ' =$$'
      )

    _x, _p, _q = symbols('x, p, q')
    
    p = latex2sympy(p_text)
    q = latex2sympy(q_text)
    
    resultado, residuo = div(p, q)

    print(
        '$$=' + 
        latex(resultado) + 
        r' + \frac{ '+ latex(residuo) +' }{ ' +  latex(q) + '}' + 
        '$$'
      )
      
    print("\n\n")
      
    operacion = p/q
    
    for valor in lis:
   
      print(
        "$$ f(" + str(valor) + r") = \frac{" + latex(p.subs(_x, valor)) + "}{" + 
        latex(q.subs(_x, valor)) + r"} = " + latex(resultado.subs(_x, valor)) + 
        r" + \frac{" + latex(residuo.subs(_x, valor)) + "}{" + 
        latex(q.subs(_x, valor)) + "} = " + latex((p/q).subs(_x, valor)) + " $$"
      )
      
    return
    

    """  
    
    
    _v = [
      "p({}) = {}".format(valor, latex(p.subs(_x, valor))) for valor in lis
      ]
    
    print('\n\n\n$$'+' \qquad '.join(_v)+'$$')
    
    
    
    _v = [
      "q({}) = {}".format(valor, latex(q.subs(_x, valor))) for valor in lis
      ]
    
    print('\n\n\n$$'+' \qquad '.join(_v)+'$$')
    
    
    
    _v = [
      "residuo({}) = {}".format(valor, latex(residuo.subs(_x, valor))) for valor in lis
      ]
    
    print('\n\n\n$$'+' \qquad '.join(_v)+'$$')

    

    """
    
    
    _v = [
      "f({}) = {}".format(valor, latex(operacion.subs(_x, valor))) for valor in lis
      ]
    
    print('\n\n\n$$'+' \qquad '.join(_v)+'$$')
    
    
def listToLatex(lista:list):
  """"""

  lista = [latex(valor) for valor in lista]
  
  return (r' \left( ' + ', '.join(lista) + r' \right)')


def setToLatex(lista:list):
  """"""

  lista = [latex(valor) for valor in lista]
  
  return (r' \left\lbrace ' + ', '.join(lista) + r' \right\rbrace')
