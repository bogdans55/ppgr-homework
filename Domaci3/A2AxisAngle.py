import numpy as np
import math
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)
 
def A2AxisAngle_netacno(A):

    if not np.allclose(np.dot(A, A.T), np.eye(3)):
        return "Nije matrica kretanja!"

    X = A - np.eye(3)

    r = [X[0][0], X[0][1], X[0][2]]
    q = [X[1][0], X[1][1], X[1][2]]

    p = np.cross(q, r)

    if p[0] == 0 and p[1] == 0 and p[2] == 0: 
        q = [[X[2][0], X[2][1], X[2][2]]]

    pnorm = math.sqrt(p[0]**2 + p[1]**2 + p[2]**2)
    p = p * (1/pnorm) 

    rnorm = math.sqrt(r[0]**2 + r[1]**2 + r[2]**2)
    u = [r[0]*1/rnorm, r[1]*1/rnorm, r[2]*1/rnorm]

    uprim = np.dot(A, u)

    cos_phi = np.dot(u, uprim)
    phi = math.acos(cos_phi)

    if np.linalg.det(np.array([p, r, q])) < 0:
        p = -p
 
    pphi = np.array([p[0], p[1], p[2],phi])  # osa i ugao idu u jedan vektor
    pphi = np.where(np.isclose(pphi, 0) , 0 , pphi)  # izbegavanje -0. u rezultatu
    return pphi



def A2AxisAngle(A):
    if not np.allclose(np.dot(A, A.T), np.eye(3)):
        return "Nije matrica kretanja!"

    phi = np.arccos((np.trace(A) - 1) / 2)

    p = 1 / (2 * np.sin(phi) + 1e-10) * np.array([A[2, 1] - A[1, 2], A[0, 2] - A[2, 0], A[1, 0] - A[0, 1]])

    pphi = np.array([p[0], p[1], p[2],phi])  # osa i ugao idu u jedan vektor
    pphi = np.where(np.isclose(pphi, 0) , 0 , pphi)  # izbegavanje -0. u rezultatu
    return pphi


# A = (1/9)*np.array([[1,-8,-4], [4,4,-7], [8,-1,4]])
# print(A2AxisAngle(A))
# print(A2AxisAngle_netacno(A))

	
# A = (1/9)*np.array([[1,-8,-4], [4,4,-7], [8,-1,5]])  #primetite 4->5, matrica A nije ortogonalna
# print(A2AxisAngle(A))
# print(A2AxisAngle_netacno(A))

# A = np.array([[0,1,0], [0,0,1], [1,0,0]]) # uporediti sa primerom za Rodrigeza sa casa, nije bas isto
# print(A2AxisAngle(A))
# print(A2AxisAngle_netacno(A))

# A = np.array([[1,0,0], [0,1,0], [0,0,1]])
# print(A2AxisAngle(A))
# print(A2AxisAngle_netacno(A))