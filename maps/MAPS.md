## Maps:
systems that operate in discrete time and space. Time only exists in that dynamical system at discrete intervals. it doesn't make sense to ask what the state of the system is in between the samples. E.g., Monthly economic indicators are like this as are old-fashioned movies which were shot at twenty-four frames per second. There was no picture of the state of the system in between those frames. Maps’ dynamics are representative but the math is a lot easier.

- Difference Equation: ${X_{n+1}} = Map ({X_n})$
- A map is a discrete time system. Time makes no sense, in between iterates.
- Maps can have many state variables.


## Logistic Equation (Iterated Map):
###
A logistic map maps the unit interval to itself:

${X_{n+1}} = {RX_n(1 - X_n)} = {RX_n - RX_n^2}$



The itinerary, or orbit, would be a list of numbers. X is a single state variable, and r is a population parameter:

${0 < x < 1}$

${N : {0,1,2,3,4,…}}$

${R : (0,4)}$

R at max is 4 before the map blows up.


# Henon Map 
It has two state variables. And returns two outputs. So the state of the systems is a Vector: ${[x_n,y_n] -> [x_{n+1},y_{n+1}]}$
- The itinerary or orbit would have a list of two numbers:
    - ${X_{n+1} = Y_{n+1} – aX_n^2}$
    - ${Y_{n+1} = bX_n}$
- X and Y are variables and a and b are parameters
- Irrespective of changing initial values, changing parameter values will lead the equation to chaos or periodic behavior.
