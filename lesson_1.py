import numpy as np
import matplotlib.pyplot as plt

# Початковий вектор
x = np.array([2, 1])

# 1. Зменшення вектора x в 2 рази по осі OX та збільшення в 3 рази по осі OY
A1 = np.array([
    [0.5, 0],
    [0, 3]
])
x1 = A1.dot(x)

# 2. Відображення вектора x відносно початку координат
A2 = np.array([
    [-1, 0],
    [0, -1]
])
x2 = A2.dot(x)

# 3. Перенесення вектора на -3 по осі OX та на 1 по осі OY
translation = np.array([-3, 1])
x3 = x + translation

# 4. Зміщення вектора x на 60° по осі OY
theta = np.radians(60)
A4 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])
x4 = A4.dot(x)

# 5. Повернення вектора x на 30°
theta = np.radians(30)
A5 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta), np.cos(theta)]
])
x5 = A5.dot(x)

# 6. Об'єднання перетворень з кроків 1, 2, 4, 5 в одну матрицю
A_combined = A5.dot(A4).dot(A2).dot(A1)
x_combined = A_combined.dot(x)

# Створення графіку
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal', 'box')

# Відображення векторів
ax.quiver(0, 0, x[0], x[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Original x')
ax.quiver(0, 0, x1[0], x1[1], angles='xy', scale_units='xy', scale=1, color='green', label='Scaled x')
ax.quiver(0, 0, x2[0], x2[1], angles='xy', scale_units='xy', scale=1, color='red', label='Reflected x')
ax.quiver(0, 0, x3[0], x3[1], angles='xy', scale_units='xy', scale=1, color='purple', label='Translated x')
ax.quiver(0, 0, x4[0], x4[1], angles='xy', scale_units='xy', scale=1, color='orange', label='Rotated 60° x')
ax.quiver(0, 0, x5[0], x5[1], angles='xy', scale_units='xy', scale=1, color='brown', label='Rotated 30° x')
ax.quiver(0, 0, x_combined[0], x_combined[1], angles='xy', scale_units='xy', scale=1, color='black', label='Combined Transform x')

# Додавання сітки
ax.grid(True)

# Додавання легенди
ax.legend()

# Показ графіку
plt.show()
