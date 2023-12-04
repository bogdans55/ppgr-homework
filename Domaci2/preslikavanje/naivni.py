import numpy as np
np.set_printoptions(precision=5, suppress=True)

def provera(points):
    minors = []
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                submatrix = points[[i, j, k]]
                minor = np.linalg.det(submatrix)
                minors.append(abs(minor))
    return min(minors)

def determinanta(a, b, c, d, e, f, g, h, i):
    return a*e*i + b*f*g + c*d*h - g*e*c - h*f*a - b*d*i
 
def naivni(origs, imgs):
    a, b, c, d = origs
    ap, bp, cp, dp = imgs

    if provera(np.array(origs)) < 1e-6:
        return "Losi originali!"
    if provera(np.array(imgs)) < 1e-6:
        return "Lose slike!"

    mat1 = [[0,0,0], [0,0,0], [0,0,0]]

    dx = determinanta(d[0], b[0], c[0], d[1], b[1], c[1], d[2], b[2], c[2])
    dy = determinanta(a[0], d[0], c[0], a[1], d[1], c[1], a[2], d[2], c[2])
    dz = determinanta(a[0], b[0], d[0], a[1], b[1], d[1], a[2], b[2], d[2])
    d = determinanta(a[0], b[0], c[0], a[1], b[1], c[1], a[2], b[2], c[2])

    l1 = dx/d
    l2 = dy/d
    l3 = dz/d

    mat1[0][0] = l1*a[0]
    mat1[1][0] = l1*a[1]
    mat1[2][0] = l1*a[2]
    mat1[0][1] = l2*b[0]
    mat1[1][1] = l2*b[1]
    mat1[2][1] = l2*b[2]
    mat1[0][2] = l3*c[0]
    mat1[1][2] = l3*c[1]
    mat1[2][2] = l3*c[2]

    mat2 = [[0,0,0], [0,0,0], [0,0,0]]

    dxp = determinanta(dp[0], bp[0], cp[0], dp[1], bp[1], cp[1], dp[2], bp[2], cp[2])
    dyp = determinanta(ap[0], dp[0], cp[0], ap[1], dp[1], cp[1], ap[2], dp[2], cp[2])
    dzp = determinanta(ap[0], bp[0], dp[0], ap[1], bp[1], dp[1], ap[2], bp[2], dp[2])
    dp = determinanta(ap[0], bp[0], cp[0], ap[1], bp[1], cp[1], ap[2], bp[2], cp[2])

    l1p = dxp/dp
    l2p = dyp/dp
    l3p = dzp/dp

    mat2[0][0] = l1p*ap[0]
    mat2[1][0] = l1p*ap[1]
    mat2[2][0] = l1p*ap[2]
    mat2[0][1] = l2p*bp[0]
    mat2[1][1] = l2p*bp[1]
    mat2[2][1] = l2p*bp[2]
    mat2[0][2] = l3p*cp[0]
    mat2[1][2] = l3p*cp[1]
    mat2[2][2] = l3p*cp[2]

    P1 = np.array(mat1)
    P2 = np.array(mat2)

    mat = np.dot(P2, np.linalg.inv(P1))
    return mat / mat[2][2]
 

trapez = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1]] 
pravougaonik = [[- 2, - 1, 1], [2, - 1, 1], [2, 1, 1], [- 2, 1, 1]]
print(naivni(trapez, pravougaonik))

origs = [[- 3, - 1, 1], [3, - 1, 1], [1, 1, 1], [- 1, 1, 1]] 
imgs = [[- 2, - 5, 1], [2, - 5, 1], [2, 1, 1], [6, -3, 3]]   #primetite da nisu u opstem polozaju
print(naivni(origs, imgs))