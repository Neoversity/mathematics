
# Завдання 1

import sympy as sp

# Задаємо змінну x
x = sp.symbols('x')

# Визначаємо функції
f = x**3 / 3 + x**2 / 2 - 2 * x
y = sp.sqrt(x**2 + 1)
h = 1 / sp.sqrt(x**2 + 1)

# Знаходимо похідні
f_prime = sp.diff(f, x)
y_prime = sp.diff(y, x)
h_prime = sp.diff(h, x)

# Обчислюємо значення похідних у точках x = 1 і x = -1/2
f_prime_at_1 = f_prime.subs(x, 1)
f_prime_at_neg_half = f_prime.subs(x, -1/2)

y_prime_at_1 = y_prime.subs(x, 1)
y_prime_at_neg_half = y_prime.subs(x, -1/2)

h_prime_at_1 = h_prime.subs(x, 1)
h_prime_at_neg_half = h_prime.subs(x, -1/2)

(f_prime, f_prime_at_1, f_prime_at_neg_half,
 y_prime, y_prime_at_1, y_prime_at_neg_half,
 h_prime, h_prime_at_1, h_prime_at_neg_half)


# Друкуємо результати
print("Завдання 1:\n")

print("f'(x) =", f_prime)
print("f'(1) =", f_prime_at_1)
print("f'(-1/2) =", f_prime_at_neg_half)

print("\ny'(x) =", y_prime)
print("y'(1) =", y_prime_at_1)
print("y'(-1/2) =", y_prime_at_neg_half)

print("\nh'(x) =", h_prime)
print("h'(1) =", h_prime_at_1)
print("h'(-1/2) =", h_prime_at_neg_half)

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Шлях до вашого зображення
image_path = '/content/DZ5_1.jpg'

img = mpimg.imread(image_path)
imgplot = plt.imshow(img)
plt.axis('off')  # Прибрати осі
plt.show()

# Завдання 2

import numpy as np
import matplotlib.pyplot as plt


# Визначаємо змінну x
x = sp.symbols('x')

# Задаємо функцію y
y = -3 * x**2 + 30 * x

# Знаходимо похідну
y_prime = sp.diff(y, x)

# Обчислюємо значення похідної у точці x = 5
max_x = 5
max_y = y.subs(x, max_x)

# Функція для обчислення значень y і y_prime
y_func = sp.lambdify(x, y, 'numpy')
y_prime_func = sp.lambdify(x, y_prime, 'numpy')

# Генеруємо значення для графіка
x_vals = np.linspace(0, 10, 400)
y_vals = y_func(x_vals)
y_prime_vals = y_prime_func(x_vals)

# Побудова графіків
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='y = -3x^2 + 30x')
plt.plot(x_vals, y_prime_vals, label="y' = -6x + 30", linestyle='--')
plt.scatter(max_x, max_y, color='red', zorder=5)
plt.text(max_x, max_y, f'Maximum: ({max_x}, {max_y})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')

# Додаємо заголовки та легенду
plt.title('Функція та її похідна')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Шлях до вашого зображення
image_path = '/content/DZ5_2.jpg'

img = mpimg.imread(image_path)
imgplot = plt.imshow(img)
plt.axis('off')  # Прибрати осі
plt.show()