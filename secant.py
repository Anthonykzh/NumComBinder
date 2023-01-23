import numpy as np
def secant(f, x0, x1, tol):
    x = x1
    it = 0
    while abs(f(x)) > tol:   # iterate until less than or eq tol
        x_prev = x
        x = x - f(x)*(x-x0)/(f(x)-f(x0))
        x0 = x_prev
        it += 1
    return x, it
