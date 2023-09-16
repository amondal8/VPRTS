import random
from sklearn import preprocessing as im
import pyautogui as pg
import utilities as ut
import utilities_dataset as ut_ds
import contextualComparison_usingdb as cc
import numpy as np
import matplotlib.pyplot as plt

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

# animal =['donkey', 'monkey']
#
# for i in range(50):
#
#     # pg.write(f'You are a {random.choice(animal)}')
#     pg.write("I love u")
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



query = f"select us_desc from userstory"
result = ut.running_searchqury(query)
list1 = list2 = ut.createlist_fromdbresult(result,0)
mat = [[0 for i in range(len(list1))] for j in range(len(list1))]
# for indi,i in enumerate(list1):
#     print(f"{indi}{i}")

for indi, i in enumerate(list1):
    for indj, j in enumerate(list2):
        simval = cc.textsimilarity(i, j)
        if simval < 0:
            simval = 0
        mat[indi][indj] = simval
#
for i in mat:
    print(i)
