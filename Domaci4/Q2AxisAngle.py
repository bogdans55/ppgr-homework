import numpy as np
from numpy import linalg
import math
np.set_printoptions(precision=5, suppress=True) 

# pomocne funkcije, ako treba


def Q2AxisAngle(q):
    qnorm = math.sqrt(q[0]**2 + q[1]**2 + q[2]**2 + q[3]**2)
    q = q * (1/qnorm) 

    if q[3] < 0:
        q = -q

    phi = 2*math.acos(q[3])

    if(abs(q[3]) == 1):
        # p = (1, 0, 0)
        pphi = np.array([1, 0, 0, 0])  # osa i ugao idu u jedan vektor. Naravno, vas kod moze biti drugaciji
        pphi = np.where(np.isclose(pphi, 0) , 0 , pphi)  # izbegavanje -0. u rezultatu
        return pphi
    else:
        xyznorm = math.sqrt(q[0]**2 + q[1]**2 + q[2]**2)
        p = [q[0]*1/xyznorm, q[1]*1/xyznorm, q[2]*1/xyznorm]

    pphi = np.array([p[0],p[1],p[2],phi])  # osa i ugao idu u jedan vektor. Naravno, vas kod moze biti drugaciji
    pphi = np.where(np.isclose(pphi, 0) , 0 , pphi)  # izbegavanje -0. u rezultatu
    return pphi
 
# ocigledno je rotacija oko Ox ose za ugao pi/4 = 0.7854
q = np.array([np.sin(np.pi/8), 0,0, np.cos(np.pi/8)])
print(Q2AxisAngle(q))

# kvaternion nije duzine 1, potrebno ga je prvo normirati
q = np.array([1,5,1,3])
print(Q2AxisAngle(q))

q = np.array([0,0,0,-3])
print(Q2AxisAngle(q))