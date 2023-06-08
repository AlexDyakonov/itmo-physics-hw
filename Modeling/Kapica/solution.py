import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Задание параметров
m = 0.1  # масса грузика, кг
l = 0.2  # длина стержня, м
delta = 0.1  # коэффициент трения
gamma = 1.0  # амплитуда внешней силы
g = 9.81
omega = 2.0 * np.sqrt(g / l)  # частота внешней силы

# Функция, описывающая уравнение движения маятника Капицы
def pendulum_eq(y, t, delta, gamma, omega, m, l):
    x, dx = y  # x - угол отклонения, dx - производная угла (скорость)
    # dydt - производная от состояния системы (скорость и ускорение)
    dydt = [dx, -delta*dx - np.sin(x) + gamma*np.cos(omega*t)/(m*l)]
    return dydt

# Задание начальных условий
y0 = [np.pi - 0.1, 0.0]  # начальное отклонение и начальная скорость

# Создание временного ряда
t = np.linspace(0, 20, num=800)

# Решение уравнения движения с использованием метода Рунге-Кутты
solution = odeint(pendulum_eq, y0, t, args=(delta, gamma, omega, m, l))

# Построение фазового портрета НЕВЕРНО, СТРОИЛ В WOLFRAM
plt.figure()  # создание нового графика
plt.plot(solution[:, 0], solution[:, 1])  # отображение x от dx/dt
plt.xlabel('x')  
plt.ylabel('dx/dt')  
plt.title('Phase portrait')  
plt.savefig('phase_portrait.png')  

# Построение графиков потенциальной и кинетической энергии в зависимости от времени
kinetic_energy = 0.5*m*l**2*solution[:, 1]**2  # кинетическая энергия = Iω^2/2, где I - момент инерции (ml^2 для маятника), ω - угловая скорость
potential_energy = m*9.81*l*(1-np.cos(solution[:, 0]))  # потенциальная энергия = mgh, где h = l(1-cosθ)

plt.figure()  # создание нового графика
plt.plot(t, kinetic_energy, label='Kinetic Energy')  # отображение времени от кинетической энергии
plt.plot(t, potential_energy, label='Potential Energy')  # отображение времени от потенциальной энергии
plt.xlabel('t')  
plt.ylabel('Energy')  
plt.title('Energy vs time')  
plt.legend()  
plt.savefig('energy_time.png')  
plt.show()  