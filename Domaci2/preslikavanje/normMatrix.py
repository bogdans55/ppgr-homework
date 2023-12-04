import numpy as np
from numpy import linalg
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

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1], [1,2,3], [-8,-2,1]] 
print(normMatrix(trapez))

# [[ 0.44969  0.       0.5746 ]
#  [ 0.       0.44969  0.09993]
#  [ 0.       0.       1.     ]]