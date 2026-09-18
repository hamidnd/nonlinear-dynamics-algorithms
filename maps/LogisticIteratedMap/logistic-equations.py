# X_n+1 = R * X_n(1 - X_n) = R*X_n - R*X_n^2
def logisticEquation(r, x0, ntime):
    output = {}
    x_next = x0
    for i in range(ntime):
        x_next = r * x_next * (1 - x_next)
        output[i] = x_next
    return x_next


def logisticEquation_trajectory(r, x0, ntime):
    output = {}
    x_next = x0
    for i in range(ntime):
        x_next = r * x_next * (1 - x_next)
        output[i] = x_next
    return output


def iterated_cosine(x0, ntime):
    import math
    xnext = x0
    for i in range(ntime):
        xnext = math.cos(math.radians(xnext))
    return xnext


def iterated_cosine_trajectory(x0, ntime):
    import math
    xnext = x0
    traj = []
    for i in range(ntime):
        xnext = math.cos(math.radians(xnext))
        traj.append(xnext)
    return traj
