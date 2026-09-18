from .. import ode_fieldVector
from ..ExplicitSolvers import forwardEuler_RK1

def backwardEuler_SHO(ic, timestep, finalTimeStep):    
    
    trajectories={}
    trajectories[0]=ic
    laststate=ic
    iterations=int(finalTimeStep/timestep)
    for i in range(iterations):
        
        # get the last field vector
        fv=trajectories[i] 
        our_guess = forwardEuler_RK1.forward_Euler_SHO_default(fv, timestep, timestep)  
        
        # now in each step we calculate the FE for just that step
        (xprime,vprime) = ode_fieldVector.ode_derivativeof_fieldVector_SHO(our_guess[0]) 
        # Forward_Euler_SHO((-1,-2), 0.1,0.1)[0] for the last state 
        
        directionslop=(timestep*xprime, timestep*vprime)
        next_position=(directionslop[0]+fv[0], directionslop[1]+fv[1])
        trajectories[i+1]=next_position
        laststate=next_position
    return (laststate, trajectories)