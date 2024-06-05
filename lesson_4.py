# # Присвоєння значень
# X = True # Присвоїмо логічне значення "Істина"
# print(X)
# Y = False # Присвоїмо логічне значення "Хибність"
# print(Y)
# print(type(X)) #Виведемо тип логічної змінної


# # Програмування таблиці істинності
# X_arr=[False,True,False,True]
# Y_arr=[False,False,True,True]
# print("# | X | Y | X | X∧Y ")
# for i in range(len(X_arr)):
#  print(f"{i+1}|{X_arr[i]}|{Y_arr[i]}|{X_arr[i] and Y_arr[i]}|{X_arr[i] or Y_arr[i]}|")


# num_set = {1, 1, 2, 2, 3, 4, 5, 6}
# print(num_set)

# months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
# # Чи належить елемент "May" множині months
# print("May" in months)

# print("1" in months)


# Об'єднання  множин з елементами числами
x = {1, 2, 3, 4}
y = {4, 3, 6}
z = {7, 4, 9, 10}


print(x | y | z)

