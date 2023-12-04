def osmoteme(vektor):
    def vektorski_proizvod(v1, v2):
        x1 = v1[1]*v2[2] - v1[2]*v2[1]
        x2 = v1[2]*v2[0] - v1[0]*v2[2]
        x3 = v1[0]*v2[1] - v1[1]*v2[0]

        return (x1, x2, x3)
    v5, v6, v7, v8, v1, v2, v3 = vektor

    v1.append(1)
    v2.append(1)
    v3.append(1)
    v5.append(1)
    v6.append(1)
    v7.append(1)
    v8.append(1)

    v21 = vektorski_proizvod(v2, v1)
    v65 = vektorski_proizvod(v6, v5)
    v78 = vektorski_proizvod(v7, v8)
    
    Yb1 = vektorski_proizvod(v21, v65)
    Yb2 = vektorski_proizvod(v21, v78)
    Yb3 = vektorski_proizvod(v65, v78)

    Ybx1 = (Yb1[0] + Yb2[0] + Yb3[0])/3
    Ybx2 = (Yb1[1] + Yb2[1] + Yb3[1])/3
    Ybx3 = (Yb1[2] + Yb2[2] + Yb3[2])/3

    Yb = (Ybx1, Ybx2, Ybx3)

    v73 = vektorski_proizvod(v7, v3)
    v62 = vektorski_proizvod(v6, v2)
    v51 = vektorski_proizvod(v5, v1)

    Xb1 = vektorski_proizvod(v73, v62)
    Xb2 = vektorski_proizvod(v73, v51)
    Xb3 = vektorski_proizvod(v62, v51)

    Xbx1 = (Xb1[0] + Xb2[0] + Xb3[0])/3
    Xbx2 = (Xb1[1] + Xb2[1] + Xb3[1])/3
    Xbx3 = (Xb1[2] + Xb2[2] + Xb3[2])/3

    Xb = (Xbx1, Xbx2, Xbx3)

    vYb3 = vektorski_proizvod(Yb, v3)
    vXb8 = vektorski_proizvod(Xb, v8)

    nevidljiva = vektorski_proizvod(vYb3, vXb8)
    return [round(nevidljiva[0]/nevidljiva[2]), round(nevidljiva[1]/nevidljiva[2])]

t7 = [32, 70]
t6 = [195, 144]
t2 = [195, 538]
t3 = [30, 307]
t8 = [251, 40]
t5 = [454, 78]
t1 = [455, 337]

print(osmoteme([t5, t6, t7, t8, t1, t2, t3]))