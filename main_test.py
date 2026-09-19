from flows.OrdinaryDifferentialEquationSolvers.SinglestepSolvers.ode_fieldVector import ode_derivativeof_fieldVector_SHO
from flows.OrdinaryDifferentialEquationSolvers.SinglestepSolvers.ExplicitSolvers.forwardEuler_RK1 import forward_Euler_SHO_default, forward_Euler_SHO
from flows.OrdinaryDifferentialEquationSolvers.SinglestepSolvers.ImplicitSolvers.backwardEuler_RK1 import backwardEuler_SHO


# python main_test.py
if __name__ == "__main__":

    print('\n','='*20,'ode_derivativeof_fieldVector_SHO:' )
    print(ode_derivativeof_fieldVector_SHO((-1, -2)))    

    print('\n','='*20,'forward_Euler_SHO_default:' )
    print('\n',forward_Euler_SHO_default((-1, -2), 0.1, 1)[0])
    
    print('\n','='*20,'forward_Euler_SHO_default and IC at (-1, -2):' )
    print('\n',forward_Euler_SHO_default((-1, -2), 0.1,  0.5, True))

    print('\n','='*20,'forward_Euler_SHO_default with bigger time step:' )
    print('\n',forward_Euler_SHO_default((-1, -2), 0.2, 0.5, True))

    print('\n','='*20,'Time Complexity of forward_Euler_SHO with 1000 iterations:' )
    print('\n',forward_Euler_SHO_default((-1, -2), 0.2, 1000, True)[2])

    # k= 2, m= 1, g=0, betha =0
    print('\n','='*20,'forward_Euler with customized SHO parameters:' )
    print('\n',forward_Euler_SHO((-1, -2), 0.05, 0.5, 2, 1, 0, 0))
    
    print('\n','='*20,'backwardEuler_SHO with IC at (-1,-2)' )
    print('\n',backwardEuler_SHO((-1,-2), 0.1,0.5))