import math as mt
from scipy.integrate import quad
P0 = 100000
V0 = 1
def p1(v):
    return P0 * mt.exp(1.5*(V0-v))
def p2(v):
    return 2 * P0 * mt.atan(3*v/2*V0)
def p3(v):
    return P0 * mt.tan(3*v/2*V0)
def p4(v):
    return P0 * mt.atan(3*v/2*V0)
a = round(quad(p1, V0, 0.6866)[0] + quad(p2, 0.6866, 2.9043)[0] + quad(p3, 2.9043, 2.7112)[0] + quad(p4, 2.7112, V0)[0], 4)
q1 = round(quad(p2, 0.6866, 2.9043)[0], 4)
ef = round(a/q1 * 100, 2)
print('Работа, совершенная газом равна ' + str(a))
print('Теплота, переданная газу в ходе цикла равна ' + str(q1))
print('КПД цикла равен ' + str(ef))