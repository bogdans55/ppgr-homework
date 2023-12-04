import numpy as np
from numpy import linalg  #zbog SVD algoritma
np.set_printoptions(precision=5, suppress=True)
 
def DLT(origs, imgs):
    A = [[0 for x in range(9)] for y in range(2*len(origs))]

    for i in range(len(origs)):
        A[2*i][0] = 0
        A[2*i][1] = 0
        A[2*i][2] = 0
        A[2*i][3] = -imgs[i][2] * origs[i][0]
        A[2*i][4] = -imgs[i][2] * origs[i][1]
        A[2*i][5] = -imgs[i][2] * origs[i][2]
        A[2*i][6] = imgs[i][1] * origs[i][0]
        A[2*i][7] = imgs[i][1] * origs[i][1]
        A[2*i][8] = imgs[i][1] * origs[i][2]

        A[2*i+1][0] = imgs[i][2] * origs[i][0]
        A[2*i+1][1] = imgs[i][2] * origs[i][1]
        A[2*i+1][2] = imgs[i][2] * origs[i][2]
        A[2*i+1][3] = 0
        A[2*i+1][4] = 0
        A[2*i+1][5] = 0
        A[2*i+1][6] = -imgs[i][0] * origs[i][0]
        A[2*i+1][7] = -imgs[i][0] * origs[i][1]
        A[2*i+1][8] = -imgs[i][0] * origs[i][2]

    u, s, vh = np.linalg.svd(A)

    mat = vh[len(vh) - 1].reshape(3, 3)
    return mat / mat[2, 2]

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1], [1,2,3], [-8,-2,1]] 
pravougaonik1 = [[- 2, - 1, 1], [2, - 1, 1], [2, 1, 1], [- 2, 1, 1], [2,1,5], [-16,-5,5]]
print(DLT(trapez, pravougaonik1))

# [[ 0.99611  0.16558 -0.19689]
#  [ 0.02513  0.96444 -0.52778]
#  [-0.07233 -0.53789  1.     ]]
