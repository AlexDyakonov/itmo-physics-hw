import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Задание параметров
delta = 0.1  # коэффициент трения
gamma = 1.0  # амплитуда внешней силы
omega = 2.0  # частота внешней силы

# Функция, описывающая уравнение движения маятника Капицы
def pendulum_eq(y, t, delta, gamma, omega):
    x, dx = y  # x - угол отклонения, dx - производная угла (скорость)
    # dydt - производная от состояния системы (скорость и ускорение)
    dydt = [dx, -delta*dx - np.sin(x) + gamma*np.cos(omega*t)]
    return dydt

# Задание начальных условий
y0 = [np.pi - 0.1, 0.0]  # начальное отклонение и начальная скорость

# Создание временного ряда
t = np.linspace(0, 50, num=2000)

# Решение уравнения движения с использованием метода Рунге-Кутты
solution = odeint(pendulum_eq, y0, t, args=(delta, gamma, omega))

# Построение фазового портрета
plt.figure()  # создание нового графика
plt.plot(solution[:, 0], solution[:, 1])  # отображение x от dx/dt
plt.xlabel('x')  # подпись оси X
plt.ylabel('dx/dt')  # подпись оси Y
plt.savefig('phase_portrait.png')  # сохранение графика в файл
plt.title('Phase portrait')  # заголовок графика

# Построение графиков потенциальной и кинетической энергии в зависимости от времени
kinetic_energy = 0.5*solution[:, 1]**2  # кинетическая энергия = mv^2/2
potential_energy = 1.0 - np.cos(solution[:, 0])  # потенциальная энергия = mgh

plt.figure()  # создание нового графика
plt.plot(t, kinetic_energy, label='Kinetic Energy')  # отображение времени от кинетической энергии
plt.plot(t, potential_energy, label='Potential Energy')  # отображение времени от потенциальной энергии
plt.xlabel('t')  # подпись оси X
plt.ylabel('Energy')  # подпись оси Y
plt.title('Energy vs time')  # заголовок графика
plt.legend()  # отображение легенды
plt.savefig('energy_time.png')  # сохранение графика в файл

plt.show()  # отображение графиков
