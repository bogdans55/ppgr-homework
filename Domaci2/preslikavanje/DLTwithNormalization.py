import numpy as np
from numpy import linalg  #zbog SVD algoritma
np.set_printoptions(precision=5, suppress=True)
 
def normMatrix(points):
    centroid = [0, 0, 1]
    for t in points:
        centroid[0] += t[0]/t[2]
        centroid[1] += t[1]/t[2]

    centroid[0] /= len(points)
    centroid[1] /= len(points)    

    G = [[1, 0, -centroid[0]], 
         [0, 1, -centroid[1]],
         [0, 0, 1]]     

    points1 = [[0, 0, 1] for i in range(len(points))]

    for i in range(len(points)):
        points1[i] = np.dot(G, [points[i][0]/points[i][2], points[i][1]/points[i][2], 1])

    distance = 0
    for t in points1:
        distance += np.sqrt(t[0] * t[0] + t[1] * t[1])

    distance /= len(points)

    S = [[np.sqrt(2)/distance, 0, 0], 
         [0, np.sqrt(2)/distance, 0],
         [0, 0, 1]]

    mat = np.dot(S, G)

    return mat

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

def DLTwithNormalization(origs, imgs):
    T = normMatrix(origs)
    norm_lista_tacaka = [np.dot(T, [t[0], t[1], t[2]]) for t in origs]
    norm_lista_tacaka = [[t[0], t[1], t[2]] for t in norm_lista_tacaka]

    Tp = normMatrix(imgs)
    norm_lista_slika = [np.dot(Tp, [t[0], t[1], t[2]]) for t in imgs]
    norm_lista_slika = [[t[0], t[1], t[2]] for t in norm_lista_slika]

    norm_lista_slika = []
    for i in range(len(imgs)):
        norm_lista_slika.append(np.dot(Tp, imgs[i]))

    P = DLT(norm_lista_tacaka, norm_lista_slika)

    mat = np.dot(np.dot(np.linalg.inv(Tp), P), T)
    return mat / mat[2][2]
 

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1], [1,2,3], [-8,-2,1]] 
pravougaonik1 = [[- 2, - 1, 1], [2, - 1, 1], [2, 1, 1], [- 2, 1, 1], [2,1,5], [-16,-5,5]]
print(DLTwithNormalization(trapez, pravougaonik1))

# [[ 0.99732  0.16288 -0.19592]
#  [ 0.02538  0.96398 -0.52775]
#  [-0.07202 -0.53967  1.     ]]