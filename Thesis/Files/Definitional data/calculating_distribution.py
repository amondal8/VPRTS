import numpy as np
from scipy import stats
import utilities as ut
import utilities_dataset as ut_ds
import contextualComparison_usingdb as cc
# import spacy
# #
# model1 = "en_core_web_lg"
#
# try:
#     nlp = spacy.load(model1)
# except OSError:
#     from spacy.cli import download
#
#     download(model1)
#     nlp = spacy.load(model1)




def find_distribution(list1, list2):
    l=len(list1)
    mat = [[0 for i in range(l)] for j in range(l)]
    # print(f"printing lis1********************************")
    # for i in list1:
    #     print(i)
    # print(f"Printing list2*********************************")
    # for j in list2:
    #     print(j)
    for indi, i in enumerate(list1):
        for indj, j in enumerate(list2):
            val = cc.textsimilarity(i, j)
            if val < 0:
                val = 0
            mat[indi][indj] = val

    return mat


# query = "Select us_desc from userstory;"
# res = ut.running_searchqury(query)
# res_list1 = ut.createlist_fromdbresult(res, 0)
# res_list2 = res_list1

# mat = find_distribution(res_list1, res_list2)
# for i in mat:
#     print(i)


def calculating_distribution(mat):
    median = np.median(mat)
    std_deviation = np.std(mat)
    q1 = np.percentile(mat, 25)
    q3 = np.percentile(mat, 75)
    iqr = q3 - q1
    average = np.mean(mat)

    print("Median:", median)
    print("Standard Deviation:", std_deviation)
    print("Interquartile Range (IQR):", iqr)
    print("Average (Mean):", average)

    return average, median, std_deviation, q1, q3, iqr


def convertstring_to_mat(ds_id):
    query = f"Select similarity_value from dataset where ds_id = {ds_id}"
    res = ut_ds.running_searchqury(query)
    l1 = res[0][0].split("\n")
    # print(res[0][0])

    l2 = [i.replace("[", "").replace("]", "").replace("'", "").replace("\n", "") for i in l1]
    rows = len(l2) - 1
    cols = len(l2[0].split(','))
    print(f"ds_id: {ds_id}, rows: {rows}, cols: {cols}")
    mat = [[0 for i in range(cols)] for j in range(rows)]
    l3 =[]
    for i in range(rows):
        # if indi == len(l2)-1:
        #     break
        # else:
        temp = l2[i].split(",")
        for indj, j in enumerate(temp):
            # print(f"i: {i}, j: {indj}")
            mat[i][indj] = float(j)
    return mat


def writingdistributionvalues_toexcel(ds_id, mean, median, standard_deviation, q1, q3, iqr):
    ut_ds.writeconfigs_to_excel("next", "A", ds_id)
    ut_ds.writeconfigs_to_excel("same", "B", mean)
    ut_ds.writeconfigs_to_excel("same", "C", median)
    ut_ds.writeconfigs_to_excel("same", "D", standard_deviation)
    ut_ds.writeconfigs_to_excel("same", "E", q1)
    ut_ds.writeconfigs_to_excel("same", "F", q3)
    ut_ds.writeconfigs_to_excel("same", "G", iqr)
    print("written to excel")

# ds_id = [41]
# ds_id = [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]

# for i in ds_id:
#     mat = convertstring_to_mat(i)
#     mean, median, sd, q1, q3, iqr = calculating_distribution(mat)
#     writingdistributionvalues_toexcel(i, mean, median, sd, q1, q3, iqr)