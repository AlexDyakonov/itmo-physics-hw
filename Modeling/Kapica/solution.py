import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m = 0.1  # масса груза в кг
l = 0.2  # длина стержня в м
g = 9.81  # ускорение свободного падения в м/с^2
nu = np.sqrt(g / l)  # собственная частота колебаний маятника

def kapitza_pendulum(state, t, a, omega):
    phi, phidot = state
    phidotdot = -(a*omega**2*np.cos(omega*t) + g)*np.sin(phi) / l
    return phidot, phidotdot

def energy(state, a, omega, t):
    phi, phidot = state
    kinetic = 0.5*m*(l*phidot)**2 + m*a*omega*np.sin(omega*t)*l*phidot*np.sin(phi) + 0.5*m*a**2*omega**2*np.sin(omega*t)**2
    potential = -m*g*(l*np.cos(phi) + a*np.cos(omega*t))
    return kinetic, potential

a = 0.1  # амплитуда колебаний подвеса в м
omega = 1.5*nu  # частота вынуждающих колебаний
state0 = [np.pi / 4, 0]  # начальные условия: угол отклонения и угловая скорость
t = np.linspace(0, 10, 1000)  # время

# Решаем систему дифференциальных уравнений
state = odeint(kapitza_pendulum, state0, t, args=(a, omega))

# Рассчитываем энергию
kinetic, potential = np.array([energy(s, a, omega, t) for s, t in zip(state, t)]).T

# Строим графики
fig, axes = plt.subplots(3, 1, figsize=(8, 10))

plt.plot(t, kinetic, label='Кинетическая')
plt.plot(t, potential, label='Потенциальная')
plt.legend()

plt.title('Energy vs time')  
plt.legend()  
plt.savefig('energy_time.png')  
plt.show()  