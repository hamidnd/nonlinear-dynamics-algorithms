from ..ode_fieldVector import ode_derivativeof_fieldVector_SHO


def forward_Euler_SHO_default(ic, timestep, finalTimeStep, estimation_timecomplexity=False):
    
    # The implementation is for an undamped system like an undamped 2-dimentional Simple harmonic oscillator (SHO)
    # with 2 state variables X and V
    # The solution for its ODE is a circle in state space, which is cosine and sine sequentially
    
    trajectories = {}
    trajectories[0] = ic
    laststate = ic
    iterations = int(finalTimeStep/timestep)
    o_n = 0  # the number of iterations
    
    for i in range(iterations):
        
        # get the last field vector
        fv = trajectories[i]  
        
        # our nearest guess
        # parameter values are default for SHO
        (xprime, vprime) = ode_derivativeof_fieldVector_SHO(fv)
        
        directionslop = (timestep*xprime, timestep*vprime)
        next_position = (directionslop[0]+fv[0], directionslop[1]+fv[1])
        trajectories[i+1] = next_position
        laststate = next_position
        
        # time execution order:
        if estimation_timecomplexity:
            o_n += 1            
    return (laststate, trajectories, o_n)

def forward_Euler_SHO(ic, timestep, finalTimeStep, *sho_args):
    
    trajectories={}
    trajectories[0]=ic
    laststate=ic
    iterations=int(finalTimeStep/timestep)
    o_n = 0 # the number of iterations
    for i in range(iterations):
        
        # get the last field vector
        fv=trajectories[i] 
        
        # our nearest guess 
        # non-default parameters are taken from caller
        (xprime,vprime) = ode_derivativeof_fieldVector_SHO(fv, *sho_args) 
        
        directionslop=(timestep*xprime, timestep*vprime)
        next_position=(directionslop[0]+fv[0], directionslop[1]+fv[1])
        trajectories[i+1]=next_position
        laststate=next_position        
        o_n+=1        
    return (laststate, trajectories, o_n)

