from latex2sympy2 import latex2sympy, latex2latex

tex = r"\frac{d}{dx}(x^{2}+x)"

x = latex2sympy(tex)

print(type(x))