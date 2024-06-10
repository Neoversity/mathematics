
# import matplotlib.pyplot as plt
# import numpy as np


# fig, ax = plt.subplots()


# # Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
# ax.spines[["left", "bottom"]].set_position(("data", 0))


# # Сховаємо верхню та праву лінію
# ax.spines[["top", "right"]].set_visible(False)


# # Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# # Також вимкнемо відсікання (clip_on=False) стрілок
# ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# # Сформуємо ряд значень x. 100 елементів від -10 до 10
# x = np.linspace(-10, 10., 100)


# # Додамо проміжні лінії
# ax.grid(True, linestyle='-.')


# # Сформуємо функцію y = x**2+2
# ax.plot(x, x**2+2)


# # Запускаємо малювання графіка
# plt.show()





# import matplotlib.pyplot as plt
# import numpy as np


# fig, ax = plt.subplots()


# # Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно
# ax.spines[["left", "bottom"]].set_position(("data", 0))


# # Сховати верхню та праву лінію
# ax.spines[["top", "right"]].set_visible(False)


# # Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# # Також вимкнемо відсікання (clip_on=False) стрілок
# ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
# ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# # Додамо проміжні лінії
# ax.grid(True, linestyle='-.')


# # Сформуємо ряд значень x. 100 елементів від -5 до 5
# x = np.linspace(-5, 5, 100, False)


# # Задаємо 2 частини функціональної залежності
# a = np.where(x>3, 2*x-1, np.nan)
# b = np.where((x<=3), 4, np.nan)


# # Генеруємо 2 графіки однакового кольору
# ax.plot(x,a,color='blue')
# ax.plot(x,b,color='blue')


# # Запускаємо малювання графіка
# plt.show()



import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

ax.spines[["left", "bottom"]].set_position(("data", 0))
# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)


# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей
# Також вимкнемо відсікання (clip_on=False) стрілок
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)


# Додамо проміжні лінії
ax.grid(True, linestyle='-.')


# Сформуємо ряд значень x. 100 елементів від -5 до 5
x = np.linspace(-5, 5, 100, False)


# Функціональну залежність
# ax.plot(x, 1/(x**2 + 2*x + 3))
# ax.plot(x, 1/(x**2 - 2*x + 3))
# ax.plot(x, np.sin(x) + 2)
# ax.plot(x, np.sin(x) + - 1)
# ax.plot(x, - x ** 2)
ax.plot(x, np.cos(x))
ax.plot(x, np.tan(x))
ax.plot(x, np.cot(x))

# Запускаємо малювання графіка
plt.show()





