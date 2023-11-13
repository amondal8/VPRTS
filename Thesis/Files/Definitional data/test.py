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



# query = f"select us_desc from userstory"
# result = ut.running_searchqury(query)
# list1 = list2 = ut.createlist_fromdbresult(result,0)
# mat = [[0 for i in range(len(list1))] for j in range(len(list1))]
# # for indi,i in enumerate(list1):
# #     print(f"{indi}{i}")
#
# for indi, i in enumerate(list1):
#     for indj, j in enumerate(list2):
#         simval = cc.textsimilarity(i, j)
#         if simval < 0:
#             simval = 0
#         mat[indi][indj] = simval
# #
# for i in mat:
#     print(i)


# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Sample data
# data = {
#     'Series1': [0.802325581395349,
# 0.450261780104712,
# 0.136363636363636,
# 0.732510288065844,
# 0.333333333333333,
# 0.3125,
# 0.716783216783217,
# 0.481099656357388,
# 0.766550522648084,
# 0.21,
# 0.42713567839196,
# 0.467032967032967,
# 0.22,
# 0.773049645390071,
# 0.386363636363636,
# 0.171875,
# 0.0884955752212389,
# 0.900452488687783,
# 0.828828828828829,
# 0.157894736842105,
# 0.916279069767442,
# 0.919028340080972,
# 0.0783132530120482,
# 0.645,
# 0.24,
# 0.79746835443038,
# 0.511538461538461,
# 0.57439446366782,
# 0.416666666666667,
# 0.229885057471264,
# 0.565217391304348,
# 0.590308370044053,
# 0.799196787148594,
# 0.593659942363112,
# 0.365448504983389,
# 0.33502538071066,
# 0.916666666666667,
# 0.386904761904762,
# 0.5,
# 0.152073732718894,
# 0.631178707224335,
# 0.78030303030303,
# 0.349462365591398,
# 0.8375,
# 0.266129032258065,
# 0.157142857142857,
# 0.26,
# 0.4453125,
# 0.258064516129032,
# 0.66,
# 0.105263157894737,
# 0.752252252252252,
# 0.803030303030303,
# 0.227722772277228,
# 0.29,
# 0.065,
# 0.291497975708502,
# 0.347222222222222,
# 0.190082644628099,
# 1,
# 0.84,
# 0.50251256281407,
# 0.351063829787234,
# 0.663507109004739,
# 0.101010101010101,
# 0.496598639455782,
# 0.333333333333333,
# 0.540697674418605,
# 0.0790513833992095,
# 0.726530612244898,
# 1,
# 0.670807453416149,
# 0.766233766233766,
# 0.404040404040404,
# 0.191387559808612,
# 0.150375939849624,
# 0.0878378378378378,
# 1,
# 0.34010152284264,
# 0.784172661870504,
# 0.863414634146341,
# 0.414507772020725,
# 1,
# 0.234042553191489,
# 0.58130081300813,
# 0.173684210526316,
# 1,
# 0.170984455958549,
# 0.756880733944954,
# 0.232323232323232,
# 0.481751824817518,
# 0.740740740740741,
# 0.731034482758621,
# 0.441988950276243,
# 0.668341708542714,
# 0.462962962962963,
# 0.248447204968944,
# 0.255813953488372,
# 0.510204081632653,
# 0.317241379310345
# ],
#     'Series2': [0.595014586282459,
# 0.816771210736175,
# 0.614954349884371,
# 0.931154564812941,
# 0.49646863896989,
# 0.096870724860255,
# 0.909203155302227,
# 0.105300429542312,
# 0.489242911995576,
# 0.845854720222527,
# 0.227781929968547,
# 0.647261979309324,
# 0.151639467828548,
# 0.125173407034776,
# 0.495392164512458,
# 0.0485016425690394,
# 0.523372334827484,
# 0.324864593477436,
# 0.8555466176863,
# 0.0849714696543151,
# 0.0432226740848147,
# 0.313801581314277,
# 0,
# 0.304057940427001,
# 0.280299567104017,
# 0.390366371873681,
# 0.0778641561604168,
# 0.98489030499523,
# 0.539630629176989,
# 0.604247844132646,
# 0.316831938132878,
# 0.138055014364258,
# 0.639184282007204,
# 0.486278234383236,
# 0.611229705173144,
# 0.720810551434746,
# 0.27564955743001,
# 0.710677448157353,
# 0.953148248338445,
# 0.0924876600730931,
# 0.31803734177504,
# 0.578081179930505,
# 0.515852664241724,
# 0.223023524400096,
# 0.711256711860146,
# 0.679737516423074,
# 0.752644040979331,
# 0.752269284989288,
# 0.149337684464693,
# 0.14510359896059,
# 0.2784779151841,
# 0.660675548658347,
# 0.727609088259325,
# 0.0925053744425823,
# 0.227174436129169,
# 0.699605217505492,
# 0.708352644368586,
# 0.891049781097241,
# 0.563229721240753,
# 0.0768596580184305,
# 0.901586971359449,
# 0.661440551035609,
# 0.761529399283953,
# 0.252614491974601,
# 0.991138094077549,
# 0.826712935805974,
# 0.62081769537035,
# 0.603965950333952,
# 0.753496338620755,
# 0.414915397628404,
# 0.197211503537844,
# 0.548884532407548,
# 0.386051757651583,
# 0.796724584063957,
# 0.079225048281066,
# 0.288296980490355,
# 0.275277603296107,
# 0.328330602621149,
# 0.679009466461332,
# 0.296508967845268,
# 0.052022817656628,
# 0.775417602135575,
# 0.210977947917864,
# 0.140411651735554,
# 0.866847186137865,
# 0.556878388674745,
# 0.416248114211469,
# 0.098916445933874,
# 0.516991269774343,
# 0.759926482474254,
# 0.835621797794794,
# 0.298244491401025,
# 0.310653451855009,
# 0.0954362902518479,
# 1,
# 0.458211055239105,
# 0.0728587330445367,
# 0.0185050321200681,
# 0.568160245832647,
# 0.338901845675463
# ],
#     'Series3': [0.3,
# 0.161538461538462,
# 0.24,
# 0.0583333333333333,
# 0.35,
# 0.9,
# 0.0916666666666667,
# 0.9,
# 0.383333333333333,
# 0.128571428571429,
# 0.66,
# 0.244444444444444,
# 0.8125,
# 0.84,
# 0.384615384615385,
# 0.949152542372881,
# 0.366666666666667,
# 0.527272727272727,
# 0.1,
# 0.92,
# 0.92,
# 0.625,
# 0.88,
# 0.59,
# 0.611111111111111,
# 0.5,
# 0.9,
# 0.0333333333333333,
# 0.3,
# 0.29,
# 0.5625,
# 0.788888888888889,
# 0.26,
# 0.325,
# 0.258333333333333,
# 0.230769230769231,
# 0.604395604395604,
# 0.238095238095238,
# 0.0714285714285714,
# 0.866666666666667,
# 0.58,
# 0.369369369369369,
# 0.39,
# 0.744444444444444,
# 0.219512195121951,
# 0.261904761904762,
# 0.173333333333333,
# 0.2,
# 0.8125,
# 0.8,
# 0.616666666666667,
# 0.255555555555556,
# 0.24,
# 0.875,
# 0.65,
# 0.24,
# 0.21,
# 0.12,
# 0.344444444444444,
# 0.925,
# 0.1,
# 0.24,
# 0.158333333333333,
# 0.616666666666667,
# 0.0571428571428571,
# 0.17,
# 0.28,
# 0.281818181818182,
# 0.19,
# 0.44,
# 0.757142857142857,
# 0.35,
# 0.418181818181818,
# 0.17,
# 0.914285714285714,
# 0.5875,
# 0.6,
# 0.633333333333333,
# 0.276923076923077,
# 0.628571428571429,
# 0.941176470588235,
# 0.177777777777778,
# 0.7,
# 0.8,
# 0.108333333333333,
# 0.3,
# 0.44,
# 0.85,
# 0.328571428571429,
# 0.16,
# 0.14,
# 0.585714285714286,
# 0.52,
# 0.966666666666667,
# 0.07,
# 0.453333333333333,
# 0.9625,
# 0.957142857142857,
# 0.32,
# 0.533333333333333
# ],
#     'Series4': [0.888515577275504,
# 0.336285888821014,
# 0.065668906536347,
# 0.75717776420281,
# 0.244349419670128,
# 0.397678680513134,
# 0.879657910812462,
# 0.580329871716555,
# 0.950519242516799,
# 0.131948686621869,
# 0.329260843005498,
# 0.332620647525962,
# 0.0439828955406231,
# 0.941356139279169,
# 0.254123396456933,
# 0.0916310323762981,
# 0.030543677458766,
# 0.854917532070861,
# 0.782529016493586,
# 0.0916310323762981,
# 0.845143555284056,
# 0.978924862553451,
# 0.000305436774587659,
# 0.533292608430055,
# 0.0528405620036652,
# 0.230604764813684,
# 0.549786194257789,
# 0.702504581551619,
# 0.30543677458766,
# 0.213805742211362,
# 0.355833842394624,
# 0.556811240073305,
# 0.85247403787416,
# 0.885766646304215,
# 0.444410507025046,
# 0.244349419670128,
# 1,
# 0.23885155772755,
# 0.397067806963958,
# 0.0916310323762981,
# 0.702504581551619,
# 0.88637751985339,
# 0.23885155772755,
# 0.864080635308491,
# 0.244349419670128,
# 0.0916310323762981,
# 0.0595601710445938,
# 0.201282834453268,
# 0.122174709835064,
# 0.243738546120953,
# 0.030543677458766,
# 0.706780696395846,
# 0.671350030543677,
# 0.15271838729383,
# 0.0760537568723274,
# 0.0015271838729383,
# 0.271227855833842,
# 0.397067806963958,
# 0.15271838729383,
# 0.60445937690898,
# 0.328039095907147,
# 0.397067806963958,
# 0.244349419670128,
# 0.584605986560782,
# 0.030543677458766,
# 0.610873549175321,
# 0.15271838729383,
# 0.366524129505192,
# 0.030543677458766,
# 0.755956017104459,
# 0.66188149053146,
# 0.435858277336591,
# 0.211973121563836,
# 0.30543677458766,
# 0.122174709835064,
# 0.122174709835064,
# 0,
# 0.961514966401955,
# 0.249541844838119,
# 0.439828955406231,
# 0.752290775809408,
# 0.30543677458766,
# 0.896151496640196,
# 0.0916310323762981,
# 0.596518020769701,
# 0.0916310323762981,
# 0.981979230299328,
# 0.0916310323762981,
# 0.695174098961515,
# 0.15271838729383,
# 0.244349419670128,
# 0.397067806963958,
# 0.427611484422725,
# 0.30543677458766,
# 0.549786194257789,
# 0.397067806963958,
# 0.122174709835064,
# 0.0916310323762981,
# 0.397067806963958,
# 0.15271838729383
# ]
# }
#
# df = pd.DataFrame(data)
#
# sns.pairplot(df)
# plt.show()

# query = f"Select similarity_value from dataset where ds_id = 156"
# res = ut_ds.running_searchqury(query)
# if res[0][0].strip(" ") == "":
#     print("Removed blanks")
# if res[0][0] is None:
#     print("No data")
# else:
#     print("Data Available")
#     print(res[0][0])

import utilities_dataset as ut_ds
import utilities as ut


def creating_valandwt(ds_id, rel_id = 1):
    us_tc_dict = dict()
    tccount_list = []
    query1 = f"Select us_id, us_businessvalue from userstory_datasettable where ds_id='{ds_id}' and release_id = {rel_id} order by us_id"
    print(query1)
    us_res = ut_ds.running_searchqury(query1)
    print(us_res)
    us_list = ut.createlist_fromdbresult(us_res,0)
    usbv_list = ut.createlist_fromdbresult(us_res,1)
    print(us_list)
    print(usbv_list)
    query2 = f"Select us_id, Count(tc_id) from us_tc_map where ds_id={ds_id} and us_id in({str(us_list).replace('[','').replace(']','')}) group by us_id"
    us_res1 = ut_ds.running_searchqury(query2)
    for i in us_res1:
        us_tc_dict[i[0]] = i[1]
    print(us_tc_dict)

    for i in us_list:
        tccount_list.append(us_tc_dict[i])
    print(tccount_list)

    return usbv_list, tccount_list



# Example usage
# val = [60, 100, 120]  # The values of the items
# wt = [10, 20, 30]  # The weights of the items
W = 35  # The capacity of the knapsack
#
# print(ut_ds.knapsack_01(val, wt, W))

usbv_list, tccount_list = creating_valandwt(210,1)
print(ut_ds.knapsack_01(usbv_list, tccount_list, W))

# li = [10]
# li1 = [1,2,34]
#
# all_present = all(element in li1 for element in li)
# print(all_present)