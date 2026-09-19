from flows.OrdinaryDifferentialEquationSolvers.SinglestepSolvers.ode_fieldVector import ode_derivativeof_fieldVector_SHO
from flows.OrdinaryDifferentialEquationSolvers.SinglestepSolvers.ExplicitSolvers.forwardEuler_RK1 import forward_Euler_SHO_default, forward_Euler_SHO
from flows.OrdinaryDifferentialEquationSolvers.SinglestepSolvers.ImplicitSolvers.backwardEuler_RK1 import backwardEuler_SHO


# python main_test.py
if __name__ == "__main__":

    print('\n',ode_derivativeof_fieldVector_SHO((-1, -2)))    

    print('\n',forward_Euler_SHO_default((-1, -2), 0.1,  0.5, True))

    print('\n',forward_Euler_SHO_default((-1, -2), 0.2, 0.5, True))

    print('\n',forward_Euler_SHO_default((-1, -2), 0.1, 0.1)[0])

    print('\n',forward_Euler_SHO_default((-1, -2), 0.2, 1000, True)[2])

    # k= 2, m= 1, g=0, betha =0
    print('\n',forward_Euler_SHO((-1, -2), 0.05, 0.5, 2, 1, 0, 0))
    
    print('\n',backwardEuler_SHO((-1,-2), 0.1,0.5))