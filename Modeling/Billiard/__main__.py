import utils as u
# Размеры стола(м)
Lx = 2.0
Ly = 2.0

# Луза, координаты и размер (м)
x0 = 1
y0 = 0.3
R = 0.2

# Координаты красного шарика (м)
x1 = 1
y1 = 0.8

# Координаты зеленого шарика (м)
x2 = 1
y2 = 0.8

# Радиус шариков (м)
r = 0.05

# Масса шариков (кг)
m = 0.3

# Начальная скорость шара (м/c)
v0 = 2

# Коэффициент трения (3 разных)
mu = [0.01, 0.05, 0.1]


pocket = u.Coordinates(x0, y0)

redBall = u.Ball(u.Coordinates(x1, y1), m, r)
greenBall = u.Ball(u.Coordinates(x2, y2), m, r)

print(redBall.isInsideOtherBall(greenBall))