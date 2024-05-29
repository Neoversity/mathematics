import numpy as np

# Вектори
a = np.array([1, 2, 3, 4, 5])
b = np.array([0.5, 1, 2, 3, 4])

# Сума
sum_ab = a + b
print("Сума a та b:", sum_ab)

# Різниця
diff_ab = a - b
print("Різниця a та b:", diff_ab)

# Матричний добуток a та b^T
outer_ab = np.outer(a, b)
print("Матричний добуток a та b^T:\n", outer_ab)

# Скалярний добуток a та b
dot_ab = np.dot(a, b)
print("Скалярний добуток a та b:", dot_ab)

# Добуток Адамара
hadamard_ab = a * b
print("Добуток Адамара a та b:", hadamard_ab)

# Ділення
division_ab = a / b
print("Ділення a та b:", division_ab)


