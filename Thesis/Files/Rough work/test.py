import random
from sklearn import preprocessing as im
import pyautogui as pg


def generate_adjmat_onetomany_withconfig(num_rows, num_columns, limiting_ones, config, connection_probability=1.0):


    # Initialize an empty adjacency matrix
    adjacency_matrix = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
    row_low = 0
    row_high = 0
    if config.lower() == "top":
        row_low = 0
        row_high = int(num_rows/4)
    elif config.lower() == "bottom":
        row_low = int((3*num_rows)/4)
        row_high = num_rows-1
    elif config.lower() == "center":
        row_low = int((num_rows) / 2)
        row_high = int((3 * num_rows) / 4)
    upper_lim = int(num_columns/6)
    print(f"row_low: {row_low}")
    print(f"row_high: {row_high}")
    print(f"upper_lim: {upper_lim}")

    # Keep track of "many" entities that have already been connected to a "one" entity
    used_many_entities = set()

    # Fill in the matrix based on the connection probability and max_ones_per_row
    for one_index in range(num_rows):
        if (one_index >= row_low and one_index < row_high) and (config.lower() == "top" or config.lower() == "bottom" or config.lower() == "center"):
            max_ones_per_row = upper_lim
        else:
            max_ones_per_row = random.randint(1, limiting_ones)  # Maximum number of ones per row
        # print(f"max_ones_per_row: {max_ones_per_row}")
        ones_count = 0
        for many_index in range(num_columns):
            if many_index in used_many_entities:
                continue
            if ones_count >= max_ones_per_row:
                break
            if random.random() <= connection_probability:
                adjacency_matrix[one_index][many_index] = 1
                used_many_entities.add(many_index)
                ones_count += 1

    return adjacency_matrix

# adj_mat = generate_adjmat_onetomany_withconfig(20,60,4,"bottom", 1)
# for row in adj_mat:
#     print(row)

# mat = [[1,2,3],[3,4,5]]
# for row in mat:
#     print(len(row))


# raw = [.5,.6,.2,.7]
# raw = [1,2,3,4,20]
# print(sum(raw))
# normalizer = 1/sum(raw)
# norm1 = [float(i) * normalizer for i in raw]
# norm = [float(i)/max(raw) for i in raw]
# normneg = [(float(i)-min(raw))/(max(raw)-min(raw)) for i in raw]
# # normalized_arr = im.normalize([li])
# print(norm)
# print(normneg)
# print(norm1)
# print(sum(norm1))


# l1 = ['TC212', 'TC584', 'TC293', 'TC401', 'TC481', 'TC576', 'TC62', 'TC125', 'TC191', 'TC204', 'TC23', 'TC310', 'TC351', 'TC498', 'TC544', 'TC99', 'TC358', 'TC36', 'TC436', 'TC239', 'TC586', 'TC206', 'TC384']
# l2 = ['TC212', 'TC498', 'TC310', 'TC293', 'TC586', 'TC206', 'TC191', 'TC358', 'TC481', 'TC436', 'TC584', 'TC99', 'TC23', 'TC384', 'TC62', 'TC576', 'TC351', 'TC544', 'TC239', 'TC125', 'TC204', 'TC36', 'TC401']
#
# all_present = all(element in l2 for element in l1)
# if all_present:
#     print("all same")

# animal =['monkey']
#
# for i in range(50):
#
#     pg.write(f'You are a {random.choice(animal)}')
#     # pg.write("I love u")
#     pg.press('enter')

# import spacy
#
# # Load the language model
# model = "en_core_web_lg"
#
# try:
#     nlp = spacy.load(model)
# except OSError:
#     from spacy.cli import download
#
#     download(nlp)
#     nlp = spacy.load(model)
#
# # Input texts
# text1 = "I love coding"
# text2 = "I enjoy programming"
#
# # Process the texts
# doc1 = nlp(text1)
# doc2 = nlp(text2)
#
# # Calculate similarity
# for i in range(1000):
#     similarity_score = doc1.similarity(doc2)
#
#     # Print the similarity score
#     print(f"Similarity Score: {similarity_score}")

# import abc as ABC
#
# class parent(ABC.ABC):
#     score = 5
#
#     # def __init__(self):
#     #     pass
#
#     def __init__(selfie, *args, **kwargs):
#         selfie.firstname = args
#         selfie.lastname = kwargs
#
#     def display(self):
#         score = 9
#         print(f"The name of the student is {self.lastname}, {self.firstname} with score {score}")
#
#     @ABC.abstractmethod
#     def noval(self):
#         pass
#
# class child(parent):
#     def noval(self):
#         print("instantiated")
#     # def my_method(self):
#     #     self.display()
#
# # obj1 = parent("Anil", "Dev")
# # obj2 = parent("Sunil", "Verma")
# # obj1.display()
# # obj2.display()
# obj3 = child()
# obj3.noval()

# def example(*args):
#     a,b,c=args
#
#
# def example(a,b,c):
#     print(a+b+c)
#
#
# example(a=1,b=2)
#
# my_dict = dict()
# my_set = set()
# my_list = []
# my_list.append(1)
# print(my_list)

# class Graph:
#     def __init__(self):
#        self.graph = {}
#
#     def edge(self,vertex,edge):
#         if vertex in self.graph:
#             self.graph[vertex].append(edge)
#         else:
#             self.graph[vertex] = [edge]
#     def print_graph(self):
#             print(self.graph)
#
#
# class Tree:
#     def __init__(self,value):
#         self.value = value
#         self.left_node = None
#         self.right_node = None
#
# t = Tree(1)
# t.right_node = Tree(3)
# t.left_node = Tree(2)
#
# t.right_node.left_node = Tree(6)
# t.right_node.right_node = Tree(7)
#
#
# import time
# import threading as Thread
#
#
#
#
# time.sleep(1)
#
# g = Graph()
# g.edge('A', 'B')
# g.edge('A', 'C')
# g.edge('B', 'C')
# g.print_graph()
#
# li=[3,4,45]
# li.insert(0,1)
# li.append(98)
# li.pop()
# print(li)
#
# my_Set = set()
#
# def  insertion_sort(arr):
#     for indi, i in enumerate(arr):
#         min = i
#         for j in range(indi+1, len(arr)):
#             if arr[j]<min:
#                 arr[j], arr[indi] = arr[indi], arr[j]
#
#     print(arr)
#
# arr = [2,3,5,6,-1]
# insertion_sort(arr)

# a = 1221
# a_st = str(a)
# reverse = a_st[len(a_st)::-1]
# print(int(reverse))
# if a == int(reverse):
#     print("I am palindrome")
# else:
#     print("No")


# import numpy as np
# import matplotlib.pyplot as plt
#
# # Your own list of numbers
# your_numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
#
# # Generate additional numbers with an exponential distribution
# additional_numbers = np.random.exponential(scale=2, size=len(your_numbers))
#
# # Combine the original list with the exponentially distributed numbers
# transformed_numbers = your_numbers + additional_numbers
#
# print(transformed_numbers)
# Plot the histograms
# plt.hist(your_numbers, bins=20, alpha=0.5, label='Original Numbers', color='blue')
# plt.hist(transformed_numbers, bins=20, alpha=0.5, label='Transformed Numbers', color='orange')
# plt.legend()
# plt.title('Original and Transformed Distributions')
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.show()


# a = .273123
# print(format(a,'.5f'))
#
#
# l = [1,2,3,4,5]
# t = "ani"
# print(t.find('ni')) #gives the start index or -1
# print(t.index('a')) #gives the index or error
# print('a' in t)     #gives true or false
# print(t[::1])
# print(t.upper())
# l.insert(0,100)
# print(l[::-1])
# ap=l.copy()
# print(ap)
# print(ap.count(101))
#
# an = [x for x in l if x%2 == 0]
# print(an)
#
# print(random.sample(l,3))


# inp = [9,9,9,9,9]
# inp[len(inp)-1]+=1
#
# for i in range(len(inp)-1,-1,-1):
#     if inp[i] == 10 and i!= 0:
#         inp[i] = 0
#         inp[i-1] += 1
#     if i == 0 and inp[i] == 10:
#         inp[i] = 0
#         inp.insert(0, 1)
# print(inp)

# ini = [1,2,3]
# ini.insert(0,1)
# print(ini)


ls = {1:21,2:21}
print(sum(ls.values())/len(ls))