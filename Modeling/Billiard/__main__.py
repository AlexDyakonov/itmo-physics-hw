import math
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
from utils import *

# длина стола ширина стола
Lx = 2.0
Ly = 2.0

# Координаты лузы
x0 = 1
y0 = 1

# Координаты красн. шарика
x1 = 1
y1 = 0.1

# Координаты зелен шарика
x2 = 1
y2 = 0.2

# Радиус лузы
R = 0.4

# Радиус шаров
r = 0.03

# Масса шаров
m = 0.3

# начальная скорость кр шара
V0 = 2

g = 9.8
# к-т трения
mu1 = 0.03
mu2 = 0.15
mu3 = 0.3

results = {
    mu1: dict(zip(np.linspace(0, 2 * np.pi, 360).tolist(), [-1] * 360)),
    mu2: dict(zip(np.linspace(0, 2 * np.pi, 360).tolist(), [-1] * 360)),
    mu3: dict(zip(np.linspace(0, 2 * np.pi, 360).tolist(), [-1] * 360))
}
dt = 10. / 2000
for mu, result in results.items():
    for alpha in result.keys():
        RedBall = Ball(Coordinates(x1, y1), \
                       Coordinates(V0 * math.cos(alpha), V0 * math.sin(alpha)), \
                       Coordinates(-mu * g * math.cos(alpha), -mu * g * math.sin(alpha)), \
                       m, r)
        GreenBall = Ball(Coordinates(x2, y2), Coordinates(0, 0), Coordinates(0, 0), m, r)
        Hole = Ball(Coordinates(x0, y0), None, None, None, R)
        for t in np.linspace(0, 10, 2000):
            if RedBall.isCollision(GreenBall):
                d = 0
                _alpha = 0
                if RedBall.speed.x != 0:
                    _alpha = math.atan(RedBall.speed.y / RedBall.speed.x)
                    if RedBall.speed.y > 0 and RedBall.speed.x < 0 or RedBall.speed.y < 0 and RedBall.speed.x < 0:
                        _alpha += math.pi
                    BR = RedBall.coordinates.y - RedBall.speed.y / RedBall.speed.x * RedBall.coordinates.x
                    BG = GreenBall.coordinates.y - RedBall.speed.y / RedBall.speed.x * GreenBall.coordinates.x
                    d = (BR - BG) / math.sqrt((RedBall.speed.y / RedBall.speed.x) ** 2 + 1)
                else:
                    if RedBall.speed.y > 0:
                        _alpha = math.pi / 2
                    else:
                        _alpha = -math.pi / 2
                    BR = RedBall.coordinates.x
                    BG = GreenBall.coordinates.x
                    d = BR - BG
                if abs(BR - BG) == 0:  # центральное столкновение
                    GreenBall.setSpeed(RedBall.getSpeed())
                    GreenBall.setAcceleration(RedBall.getAcceleration())
                else:  # нецентральное соударение
                    phi = math.acos(abs(d) / (2 * r)) #формула, получена аналитически
                    if _alpha != math.pi / 2: #рассчет углов, при различных случаях налета шаров
                        # вычисляются углы при соударении, дальше меняем скорости.
                        if (d > 0) == (RedBall.speed.x > 0):  # A
                            phiRed = _alpha + phi
                            phiGreen = _alpha - (math.pi / 2 - phi)
                        else:  # B
                            phiRed = _alpha - phi
                            phiGreen = _alpha + (math.pi / 2 - phi)
                    else:
                        if (BR < BG) == (RedBall.coordinates.x < GreenBall.coordinates.x):
                            phiRed = _alpha + phi
                            phiGreen = _alpha - (math.pi / 2 - phi)
                        else:
                            phiRed = _alpha - phi
                            phiGreen = _alpha + (math.pi / 2 - phi)
                    GBSpeedNorm = RedBall.speed.norm() * math.sin(_alpha - phiRed) / math.sin(phiGreen - phiRed)
                    GreenBall.setSpeed(Coordinates(GBSpeedNorm * math.cos(phiGreen), \
                                                   GBSpeedNorm * math.sin(phiGreen)))     #обновление скорости зеленого
                    GreenBall.setAcceleration(Coordinates(-mu * g * math.cos(phiGreen), -mu * g * math.sin(phiGreen)))
                    RBSpeedNorm = RedBall.speed.norm() / math.cos(phiRed) * \
                                  (math.cos(_alpha) - math.cos(phiGreen) * math.sin(_alpha - phiRed) / math.sin(
                                      phiGreen - phiRed))
                    RedBall.setSpeed(Coordinates(RBSpeedNorm * math.cos(phiRed)
                                                 , RBSpeedNorm * math.sin(phiRed)))     #обновление скорости красного
                    RedBall.setAcceleration(Coordinates(-mu * g * math.cos(phiRed), -mu * g * math.sin(phiRed)))

                    #обновление скоростей произошло после рассчета углов разлета в ДСК.
            if GreenBall.isCollision(Hole): #попадание в лузу
                result[alpha] = m * GreenBall.speed.norm() ** 2 / 2
                break
            if RedBall.speed.x == 0 and RedBall.speed.y == 0 and GreenBall.speed.x == 0 and GreenBall.speed.y == 0:
                break  # все шары остановились
            RedBall.isCollisionWall(Lx, Ly)
            GreenBall.isCollisionWall(Lx, Ly)
            RedBall.iteration(dt)
            GreenBall.iteration(dt)

    # results[mu] = {angle:energy for angle, energy in result.items() if energy != -1}

# Graph
color1 = 'white'
color2 = 'black'
color0 = color2

_results = {
    mu1: None,
    mu2: None,
    mu3: None
}
for mu in results.keys():
    arrays = []
    array = {}
    for key, value in results[mu].items():
        if value != -1:
            array.update({key: value})
        else:
            if len(array) != 0:
                arrays.append(array.copy())
                array.clear()
    _results[mu] = arrays

fig = plt.figure(figsize=(15, 10))

ax = fig.add_subplot()
plt.minorticks_on()
plt.xlim((0, 360))
plt.grid(which='major', color='grey')
plt.grid(which='minor', color='grey')
plt.ylabel("Энергия шара $E$ (Дж)", fontsize=24, color=color0)
plt.xlabel("Угол $\\alpha$ (град)", fontsize=24, color=color0)
ax.tick_params(axis='x', colors=color0)
ax.tick_params(axis='y', colors=color0)
colors = {
    mu1: 'r',
    mu2: 'g',
    mu3: 'b'
}
for mu, segments in _results.items():
    lbl = 'mu = ' + str(mu)
    for segment in segments:
        plt.plot([angle * 180 / math.pi for angle in list(segment.keys())], list(segment.values()), color=colors[mu],
                 label=lbl)
        lbl = ''
plt.legend()
plt.grid(True)

plt.savefig('Modeling\Billiard\graph.jpg')
plt.show()