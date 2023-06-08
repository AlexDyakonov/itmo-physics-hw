import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

g = 9.81  # ускорение свободного падения, м/с^2
l = 0.2  # длина стержня, м
m = 0.1  # масса грузика, кг

def pendulum_eq(y, t, delta, gamma, omega, g, l, m):
    x, v = y  # x - угол отклонения, v - угловая скорость
    dxdt = v
    dvdt = -delta*v - g/l*np.sin(x) + gamma*np.cos(omega*t)/m
    return [dxdt, dvdt]

y0 = [np.pi - 0.1, 0.0]  # начальное отклонение и начальная скорость

# Задание временного ряда
t = np.linspace(0, 50, num=5000)

frequencies = np.linspace(0.1, 3.0, 30)  # выбор диапазона значений для частоты f
amplitudes = []  # список для сохранения вычисленных амплитуд


for f in frequencies:
    omega = 2*np.pi*f  # перевод частоты в угловую скорость
    solution = odeint(pendulum_eq, y0, t, args=(0.1, 1.0, omega, g, l, m))
    amplitude = np.max(np.abs(solution[:, 0]))  # определение амплитуды как максимального значения угла отклонения
    amplitudes.append(amplitude)

# Построение графика амплитуды в зависимости от частоты
plt.figure()
plt.plot(frequencies, amplitudes)
plt.xlabel('Frequency (f)')
plt.ylabel('Amplitude (a)')
plt.title('Amplitude-Frequency Diagram')
plt.savefig('a-f_plot.png')  
plt.grid(True)
plt.show()
