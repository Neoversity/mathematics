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
# x = {1, 2, 3, 4}
# y = {4, 3, 6}
# z = {7, 4, 9, 10}


# print(x | y | z)


# import matplotlib.pyplot as plt
# from matplotlib_venn import venn3


# set1 = set([11,12,13,14,15,16,17,18,19])
# set2 = set([2,4,6,8,10,12,14,16,18])
# set3 = set([3,6,9,12,15,18])


# venn3([set1, set2, set3], ('>10', 'Парні', 'Кратні 3'))


# plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt


# # Створення пустого графа
# G = nx.Graph()


# # Додавання вершин
# G.add_nodes_from([1, 2, 3, 4, 5])


# # Додавання ребер (з'єднань між вершинами)
# G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])


# # Візуалізація графа
# pos = nx.spring_layout(G) # Визначення позицій вершин
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, edge_color='gray')
# plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt


# # Створення орієнтованого графа
# directed_graph = nx.DiGraph()
# directed_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])


# # Визначення позицій вершин для візуалізації
# pos = nx.spring_layout(directed_graph)


# # Візуалізація орієнтованого графа
# nx.draw(directed_graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray', arrowsize=20, connectionstyle="arc3,rad=0.1")


# plt.title("Directed Graph")
# plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt


# # Створення орієнтованого графа
# directed_graph = nx.DiGraph()
# directed_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (1, 4)])


# # Визначення позицій вершин для візуалізації
# pos = nx.spring_layout(directed_graph)


# # Візуалізація орієнтованого графа
# nx.draw(directed_graph, pos, with_labels=True, font_size=10, node_size=700, node_color='skyblue', font_color='black', edge_color='gray', arrowsize=20, connectionstyle="arc3,rad=0.1")


# plt.title("Directed Graph")
# plt.show()


# import networkx as nx
# import matplotlib.pyplot as plt
# import numpy as np


# def build_and_visualize_graph(incidence_matrix):
#     """
#     Функція, яка будує граф із заданої матриці інцидентності та візуалізує його.


#     Параметри:
#     - incidence_matrix: numpy.ndarray, матриця інцидентності графа.


#     Повертає:
#     - None
#     """
#     # Створення графа
#     graph = nx.Graph()
#     num_nodes, num_edges = incidence_matrix.shape


#     # Додавання вершин до графа
#     graph.add_nodes_from(range(num_nodes))


#     # Додавання ребер та їх ваг
#     for edge_index in range(num_edges):
#         edge_nodes = np.where(incidence_matrix[:, edge_index] != 0)[0]
#         if len(edge_nodes) == 2:
#             graph.add_edge(edge_nodes[0], edge_nodes[1], weight=edge_index + 1)


#     # Визначення позицій вершин для візуалізації
#     pos = nx.spring_layout(graph)


#     # Визуалізація графа
#     nx.draw(graph, pos, with_labels=True, font_size=10, node_size=700, font_color='black', edge_color='gray')


#     # Додавання ваг ребер
#     labels = nx.get_edge_attributes(graph, 'weight')
#     nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels, font_color='red')


#     plt.title("Graph from Incidence Matrix")
#     plt.show()


# # Приклад використання функції з попередньо заданою матрицею інцидентності
# example_incidence_matrix = np.array([
#     [1, 0, 0, 0, 1, 0, 0],
#     [1, 1, 0, 0, 0, 1, 0],
#     [0, 1, 1, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0, 0, 1],
#     [0, 0, 0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0, 0, 1]
# ])


# build_and_visualize_graph(example_incidence_matrix)


# Перетворення символів в ASCII-коди
text = "Hello"
ascii_codes = [ord(char) for char in text]
print("ASCII Codes:", ascii_codes)
# Перетворення ASCII-кодів в символи
decoded_text = "".join([chr(code) for code in ascii_codes])
print("Decoded Text:", decoded_text)



