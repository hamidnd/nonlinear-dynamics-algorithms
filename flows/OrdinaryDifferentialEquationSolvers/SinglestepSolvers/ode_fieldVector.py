# abstraction for derivative implementation
def ode_derivativeof_fieldVector(xFieldVector, *params):
    pass 


def ode_derivativeof_fieldVector_SHO(xFieldVector=(0,0), k= 2.0, m= 0.5, g=0, betha =0):
    (x,v) = xFieldVector
    xPrime = v
    vPrime = g-(k/m)*x - (betha/m)*v
    return (xPrime, vPrime)