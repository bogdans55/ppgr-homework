import numpy as np
import math
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)
 
def AxisAngle2A(pphi):
    p, phi = pphi[0:3], pphi[3]

    A = np.outer(p, p)
    A += math.cos(phi) * (np.eye(3) - A)
    A += math.sin(phi) *  np.array([[0, -p[2], p[1]], 
                                    [p[2], 0, -p[0]],
                                    [-p[1], p[0], 0]])
 
    A = np.where(np.isclose(A, 0) , 0.0 , A)  # izbegavanje -0. u rezultatu
    return A

# pphi = np.array([1/3, -2/3,  2/3, np.pi/2])
# print(AxisAngle2A(pphi))