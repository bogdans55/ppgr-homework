import numpy as np
import math
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)

def Euler2A(uglovi):
    psi, theta, fi = uglovi[0], uglovi[1], uglovi[2]
    
    cos_psi = math.cos(psi)
    sin_psi = math.sin(psi)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)
    cos_fi = math.cos(fi)
    sin_fi = math.sin(fi)

    A = np.array([[cos_psi * cos_theta, -sin_psi * cos_fi + cos_psi * sin_theta * sin_fi, sin_psi * sin_fi + cos_psi * sin_theta * cos_fi],
                  [sin_psi * cos_theta, cos_psi * cos_fi + sin_psi * sin_theta * sin_fi, -cos_psi * sin_fi + sin_psi * sin_theta * cos_fi],
                  [-sin_theta, cos_theta * sin_fi, cos_theta * cos_fi]])
    
    A = np.where(np.isclose(A, 0) , 0 , A)  # da bi izbegli -0. u rezultatu
    return A
 
# uglovi = np.array([np.pi/2, -np.pi/4, (7/8)*np.pi])
# print(Euler2A(uglovi))