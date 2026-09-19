# FLows
Flows are continuous time systems, dynamics that operate continuously in time and space. in continuous time systems, time proceeds smoothly. E.g., flows, differential equations in modeling tools. 
in discrete time systems (such as maps), information can only be observed in intevals (e.g., every second or so). we have no idea what it did in between. we have no idea what it did in between i.e., information is at those discrete intervals. And that's the difference between a map and a flow - discrete time vs. continuous time. in continuous systems, we might have to do a bit of discretization of time and space, if our sensors (data collectors) have a finite sample time. Snapshotting actually is discretizing the time. It is turning a flow to a map. And in fact, things are snapshots of processes. But if we think of these complicated non-linear dynamics and chaos as a static thing, then the process that such system took to grow that becomes much more explainable. both maps and flows can have many state variables.
 
 ## N-dimensional non-linear systems:
the dimension of the system is the number of state variables or is the number of first order ODE or is the number of axes in the state space. the state vector includes state variables, and this vector is a point on the state space and X’ (its first derivative) tells us given any point in the space (a vector), the slop or which direction is downhill.

## Differential Equations (ODE Models): 
the solution moves around continuously in a n-dimensional phase space. a difference equation gives us the next point. but a differential equation gives us just the direction in which the state is going to evolve, and we have to some work to get the next point (ODE solver as a computer numerical solution does this work).
Differential equations are indirect rules that specifies variables (x, y, z, …) by telling us, not x, y, or z directly, but their rates of change. The rule is “indirect” since it involves the rate of change of T and not T itself. And the time and outcome are continuous. 
- Any ODE (ordinary differential equation) that can be solved analytically is by definition not chaotic. The ODEs are good models at capturing dynamics in physics, biology, economics, …
- The order of an ordinary differential equation is the number of primes in the highest order derivative
- Only differential equations involve derivatives, and difference equations do not involve derivative.
- By definition, the velocity is the derivative of the position.
 - Lotka-Volterra (two-dimensional), RSI(sell variable and buy variable), MACD(short-term mean average variable, and long-term mean average varaibale) diagrams, are examples of two dimensional analysis
 - Lorenz and Rossler Attractors (three-dimensional) are of the examples of ODE models that show the strange attractors features (stable chaotic orbits) in n-dimensional space.

### Lotka-Volterra: 
a two-dimensional differential equation, trying to keep track of two things varying in time. the problem analysis of population of rabbits and the population of foxes is an example of this model. and this is a rule that tells us how the rabbits and foxes change over time. the Rabbit-fox interaction problem is not cyclic. solutions to the Lotka-Volterra equations is using numerical approach like Euler’s method, pretending that that rate of change is constant for a time interval, then updates the number of rabbits and foxes, and then re-evaluates the derivative and so on, such that it will get closer and closer to the solution.

${{dp/dt}= rp(1-p/k) - h}$
- R is the growth parameter
- K is carrying capacity
- H is harvesting rate; i.e. the number of fish that are caught every year.
- When h=0: 
    - At P=0, we have repeler or unstable equillibrium
    - At p=k, we have atractor or stable equillibrium

Zero change: 
in fixed points (equilibrium), because the rate of change is zero, therefore the derivative (differential equation) should be zero, we have: dx/dt = 0





