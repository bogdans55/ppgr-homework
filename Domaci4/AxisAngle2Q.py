import numpy as np
from numpy import linalg
import math
np.set_printoptions(precision=5, suppress=True) 

# pomocne funkcije, ako treba

def AxisAngle2Q(pphi):
    p, phi = pphi[0:3], pphi[3]
    
    pnorm = math.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
    p = p * (1/pnorm)
    
    w = math.cos(phi/2)
    xyz = math.sin(phi/2)*p
    x, y, z = xyz[0], xyz[1], xyz[2]
    
    
    q = np.array([x,y,z,w])  # naravno, ne mora da bude ovako
    q = np.where(np.isclose(q, 0) , 0 , q)  # izbegavanje -0. u rezultatu
    return q
 
pphi = np.array([1, 0,0, (np.pi)/2])
print(AxisAngle2Q(pphi))

pphi = np.array([1, 1,1, (2*np.pi)/3])
print(AxisAngle2Q(pphi))