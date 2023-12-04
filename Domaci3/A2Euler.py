import numpy as np
import math
from numpy import linalg  #ako vam treba
np.set_printoptions(precision=5, suppress=True)  # formatiranje izlaza na 5 decimala
 
def A2Euler(A):

    if not np.allclose(np.dot(A, A.T), np.eye(3)):
        return "Nije matrica kretanja!"
 
    if(A[2][0] < 1):
        if(A[2][0] > -1):
            psi = math.atan2(A[1][0], A[0][0])
            theta = math.asin(-A[2][0])
            phi = math.atan2(A[2][1], A[2][2])
        else:
            psi = math.atan2(-A[0][1], A[1][1])
            theta = math.pi/2
            phi = 0
    else:
        psi = math.atan2(-A[0][1], A[1][1])
        theta = -math.pi/2
        phi = 0
 
 
    uglovi = np.array([psi, theta, phi])
    uglovi = np.where(np.isclose(uglovi, 0) , 0 , uglovi)  
    return uglovi
 
A = (1/9)*np.array([[1,-8,-4], [4,4,-7], [8,-1,4]])
print(A2Euler(A))

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(A2Euler(A))