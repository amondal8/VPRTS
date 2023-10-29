import random

import utilities_dataset as ut_ds
import utilities as ut
import matplotlib.pyplot as plt


def updatebv_userstory_datasetable(ds_id):
    bv_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in ds_id:
        query = f"Select us_id from userstory_datasettable where ds_id = '{i}'"
        res = ut_ds.running_searchqury(query)
        us_list = ut.createlist_fromdbresult(res, 0)
        for j in us_list:
            value = random.choice(bv_list)
            ind = bv_list.index(value)
            fin_val = random.randint(0, ind)
            # fin_val1 = random.randint(0, fin_val)
            updatequery = f"""UPDATE userstory_datasettable
                            SET us_businessvalue = {bv_list[fin_val]}
                            WHERE ds_id = {i} and us_id ={j}; """
            ut_ds.running_insertquery(updatequery)
        print(f"Business values updated for {i}")

def plot_histogram_bv(dsid_list):
    for i in dsid_list:
        query = f"Select us_businessvalue from userstory_datasettable where ds_id = '{i}'"
        res = ut_ds.running_searchqury(query)
        print(len(res))
        res_list = ut.createlist_fromdbresult(res, 0)
        print(res_list)
        hist_data, bin_edges, _ = plt.hist(res_list, bins=9, edgecolor='black')
        print("Histogram Data:")
        print("Bin Edges:", bin_edges)
        print("Bin Counts:", hist_data)
        plt.xlabel('Business Value')
        plt.ylabel('Frequency')
        plt.title(f'Business value Histogram for ds_id: {i}')
        plt.show()
        # plt.savefig(f"C:/Users/amondal8/Desktop/Aniruddha/Thesis/Datasets/My dataset/Results/Graphs/bv_plots/bv plot_ds_id{i}")
        # plt.close()


def calculate_bv_dist(dsid_list):
    bv_dict = {}
    final = {}
    for i in dsid_list:
        query1 = f"Select  count(us_id) from userstory_datasettable where ds_id = '{i}'"
        res1 = ut_ds.running_searchqury(query1)
        query2 = f"select us_businessvalue,count(us_businessvalue)/{res1[0][0]} from userstory_datasettable where ds_id = '{i}' group by us_businessvalue order by us_businessvalue;"
        res2 = ut_ds.running_searchqury(query2)
        # print(res2)
        # print(res2[0][1])

        for j in res2:
            # print(j[0])
            if j[0] in bv_dict:
                bv_dict[j[0]] += j[1]
            else:
                bv_dict[j[0]] = j[1]
        # print(f"bv_dist: {bv_dict}")

    #
    sum_of_values = sum(bv_dict.values())
    # print(sum_of_values)
    for keys in bv_dict:
        value = format(bv_dict[keys]/sum_of_values, '.5f')
        final[keys] = value
    print(f"final: {final}")

def calculate_bv_dist_byrelease(dsid_list):
    bv_dict_r1 = {}
    bv_dict_r2 = {}
    final1 = {}
    final2 = {}
    for i in dsid_list:
        query_count_r1 = f"Select  count(us_id) from userstory_datasettable where ds_id = '{i}' and release_id = 1"
        query_count_r2 = f"Select  count(us_id) from userstory_datasettable where ds_id = '{i}' and release_id = 2"
        res1 = ut_ds.running_searchqury(query_count_r1)
        res2 = ut_ds.running_searchqury(query_count_r2)
        query1 = f"select us_businessvalue,count(us_businessvalue)/{res1[0][0]} from userstory_datasettable where ds_id = '{i}' and release_id = 1 group by us_businessvalue order by us_businessvalue;"
        query2 = f"select us_businessvalue,count(us_businessvalue)/{res2[0][0]} from userstory_datasettable where ds_id = '{i}' and release_id = 2 group by us_businessvalue order by us_businessvalue;"

        res_bvcount_r1 = ut_ds.running_searchqury(query1)
        res_bvcount_r2 = ut_ds.running_searchqury(query2)
        # print(res2)
        # print(res2[0][1])

        for j in res_bvcount_r1:
            # print(j[0])
            if j[0] in bv_dict_r1:
                bv_dict_r1[j[0]] += j[1]
            else:
                bv_dict_r1[j[0]] = j[1]
        for j in res_bvcount_r2:
            # print(j[0])
            if j[0] in bv_dict_r2:
                bv_dict_r2[j[0]] += j[1]
            else:
                bv_dict_r2[j[0]] = j[1]
        # print(f"bv_dist: {bv_dict}")

    #
    sum_of_values1 = sum(bv_dict_r1.values())
    sum_of_values2 = sum(bv_dict_r2.values())
    # print(sum_of_values)
    for keys in bv_dict_r1:
        value = format(bv_dict_r1[keys]/sum_of_values1, '.5f')
        final1[keys] = value
    for keys in bv_dict_r2:
        value = format(bv_dict_r2[keys]/sum_of_values2, '.5f')
        final2[keys] = value
    print(f"final1: {final1}")
    print(f"final2: {final2}")

def printres_fromdb(ds_id, config):
    for i in config:
        query = f"Select results_config{i} from dataset where ds_id = '{ds_id}'"
        res = ut_ds.running_searchqury(query)
        print('\n'+res[0][0])


def frequency_bv(ds_id):
    bv_dict = {}
    for i in ds_id:
        query = f"select us_businessvalue, count(us_id) from userstory_datasettable where ds_id = {i} group by us_businessvalue order by us_businessvalue "
        res = ut_ds.running_searchqury(query)
        for j in res:
            if j[0] in bv_dict:
                bv_dict[j[0]] += j[1]
            else:
                bv_dict[j[0]] = j[1]
    print(bv_dict)

def frequency_bv_byrelease(ds_id):
    bv_dict_rel1 = {}
    bv_dict_rel2 = {}
    final1 = {}
    final2 = {}
    for i in ds_id:
        query_r1 = f"select us_businessvalue, count(us_id) from userstory_datasettable where ds_id = {i} and release_id = 1 group by us_businessvalue order by us_businessvalue"
        query_r2 = f"select us_businessvalue, count(us_id) from userstory_datasettable where ds_id = {i} and release_id = 2 group by us_businessvalue order by us_businessvalue"
        res_r1 = ut_ds.running_searchqury(query_r1)
        res_r2 = ut_ds.running_searchqury(query_r2)
        for j in res_r1:
            if j[0] in bv_dict_rel1:
                bv_dict_rel1[j[0]] += j[1]
            else:
                bv_dict_rel1[j[0]] = j[1]
        for j in res_r2:
            if j[0] in bv_dict_rel2:
                bv_dict_rel2[j[0]] += j[1]
            else:
                bv_dict_rel2[j[0]] = j[1]
    sum_of_values1 = sum(bv_dict_rel1.values())
    sum_of_values2 = sum(bv_dict_rel2.values())
    # print(sum_of_values)
    for keys in bv_dict_rel1:
        value = format(bv_dict_rel1[keys] / sum_of_values1, '.5f')
        final1[keys] = value
    for keys in bv_dict_rel2:
        value = format(bv_dict_rel2[keys] / sum_of_values2, '.5f')
        final2[keys] = value


    print(f"rel1: {final1}")
    print(f"rel2: {final2}")


def frequency_bv_eachds(ds_id):
    bv_dict = {}
    for i in ds_id:
        query = f"select us_businessvalue, count(us_id) from userstory_datasettable where ds_id = {i} group by us_businessvalue order by us_businessvalue "
        res = ut_ds.running_searchqury(query)
        for j in res:
            bv_dict[j[0]] = j[1]
        print(f"ds_id: {i}")
        print(bv_dict)


def matching_testcases(dsid_list, config1, config2):
    for ds_id in dsid_list:
        us_set1 = dict()
        us_set2 = dict()
        print(f"ds_id: {ds_id}")
        query1 = f"Select results_config{config1} from dataset where ds_id = '{ds_id}'"
        query2 = f"Select results_config{config2} from dataset where ds_id = '{ds_id}'"
        print(f"query: {query1}")
        res1 = ut_ds.running_searchqury(query1)
        res2 = ut_ds.running_searchqury(query2)
        res_str1 = res1[0][0]
        res_str2 = res2[0][0]
        desired_lineno1 = 0
        desired_lineno2 = 0
        lines1 = res_str1.split('\n')
        for indi, i in enumerate(lines1):
            if "Selected test cases through our RTS process:" in i:
                desired_lineno1 = indi
                break
        lines2 = res_str2.split('\n')
        for indj, j in enumerate(lines2):
            if "Selected test cases through our RTS process:" in j:
                desired_lineno2 = indj
                break
        desired_line1 = lines1[desired_lineno1].replace("Selected test cases through our RTS process: ", "")
        desired_line2 = lines2[desired_lineno2].replace("Selected test cases through our RTS process: ", "")
        set1 = ut_ds.creatingset_fromstring(desired_line1)
        set2 = ut_ds.creatingset_fromstring(desired_line2)
        print(f"config1: {set1}")
        print(f"config2: {set2}")
        overlap_elements = set1.intersection(set2)
        print(len(overlap_elements))
        # ut_ds.readandwrite_toexcel(ds_id, "AB", len(overlap_elements))
        if len(overlap_elements) != len(set1):
            extra_elements_set1 = set1 - set2
            extra_elements_set1_list = list(extra_elements_set1)
            extra_elements_set2 = set2 - set1
            extra_elements_set2_list = list(extra_elements_set2)
            print(f"Extra elements in set2: {extra_elements_set2_list}")
            fin_query1 = f"Select us_id, us_businessvalue from userstory_datasettable where ds_id = {ds_id} and us_id in (Select distinct(us_id) from us_tc_map where tc_id in ({str(extra_elements_set1_list).replace('[','').replace(']','')}) and ds_id = '{ds_id}')"
            print(f"fin_query1: {fin_query1}")
            fin_query2 = f"Select us_id, us_businessvalue from userstory_datasettable where ds_id = {ds_id} and us_id in (Select distinct(us_id) from us_tc_map where tc_id in ({str(extra_elements_set2_list).replace('[','').replace(']','')}) and ds_id = '{ds_id}')"
            print(f"fin_query2: {fin_query2}")
            us_res1 = ut_ds.running_searchqury(fin_query1)
            us_res2 = ut_ds.running_searchqury(fin_query2)

            for l in us_res1:
                us_set1[l[0]] = l[1]
            for m in us_res2:
                us_set2[m[0]] = m[1]
        try:
            if us_set1 is not None:
                averagebv_set1 = sum(us_set1.values())/len(us_set1)
                ut_ds.readandwrite_toexcel(ds_id, "AE", averagebv_set1)
            if us_set2 is not None:
                averagebv_set2 = sum(us_set2.values()) / len(us_set2)
                ut_ds.readandwrite_toexcel(ds_id, "AF", averagebv_set2)
        except:
            print(f"skipping ds id {ds_id}")
        # print(sum(us_set1.values()))
        # print(f"len: {len(us_set1)}")


        # ut_ds.readandwrite_toexcel(ds_id, "AD", str(us_set1))
        # ut_ds.readandwrite_toexcel(ds_id, "AE", str(us_set2))

def trial(ds_id, config1, config2):
    desired_lineno1 = 0
    desired_lineno2 = 0
    query1 = f"Select results_config{config1} from dataset where ds_id = '{ds_id}'"
    query2 = f"Select results_config{config2} from dataset where ds_id = '{ds_id}'"
    # print(f"query: {query1}")
    res1 = ut_ds.running_searchqury(query1)
    res2 = ut_ds.running_searchqury(query2)
    # print(f"res1: {res1[0][0]}")
    # print(f"res1: {res2[0][0]}")
    lines1 = res1[0][0].split("\n")
    lines2 = res2[0][0].split("\n")
    for indi, i in enumerate(lines1):
        if "Selected test cases through our RTS process:" in i:
            desired_lineno1 = indi
            break
    for indj, j in enumerate(lines2):
        if "Selected test cases through our RTS process:" in j:
            desired_lineno2 = indj
            break

    set1 = ut_ds.creatingset_fromstring(lines1[desired_lineno1].replace("Selected test cases through our RTS process: ", ""))
    set2 = ut_ds.creatingset_fromstring(lines2[desired_lineno2].replace("Selected test cases through our RTS process: ", ""))
    # set1 = ut_ds.creatingset_fromstring(lines1[desired_lineno1])
    # set2 = ut_ds.creatingset_fromstring(lines2[desired_lineno2])
    print(lines1[desired_lineno1])
    print(lines2[desired_lineno2])
    print(len(set1 - set2))


# 1.1 AND 1.3 is greater
# ds_id = [145,149,164,191,206,212,236,251,255,265,290,323,326,335]
# 1.1 is greater
# Sim val greater
ds_id = [141,
142,
143,
144,
145,
146,
147,
148,
149,
150,
151,
152,
153,
154,
155,
156,
157,
158,
159,
160,
161,
162,
163,
164,
165,
166,
167,
168,
169,
170,
171,
172,
173,
174,
175,
176,
177,
178,
179,
180,
181,
182,
183,
184,
185,
186,
187,
188,
189,
190,
191,
192,
193,
194,
195,
196,
197,
198,
199,
200,
201,
202,
203,
204,
205,
206,
207,
208,
210,
209,
211,
212,
213,
214,
215,
216,
217,
218,
219,
220,
221,
222,
223,
224,
225,
226,
227,
228,
229,
230,
231,
232,
233,
234,
235,
236,
237,
238,
239,
240,
241,
242,
243,
244,
245,
246,
247,
248,
249,
250,
251,
252,
253,
254,
255,
256,
257,
258,
259,
260,
261,
262,
263,
264,
265,
266,
267,
268,
269,
270,
271,
272,
273,
274,
275,
276,
277,
278,
279,
280,
281,
282,
283,
284,
285,
286,
287,
288,
289,
290,
291,
292,
293,
294,
295,
296,
297,
298,
299,
300,
301,
302,
303,
304,
305,
306,
307,
308,
309,
310,
311,
312,
313,
314,
315,
316,
317,
318,
319,
320,
321,
322,
323,
324,
325,
326,
327,
328,
329,
330,
331,
332,
333,
334,
335,
336,
337,
338,
339,
340

]

# ds_id = [241,242]
# ds_id = [241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340]

# ds_id = [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240]

# ds_id = [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340]

# ds_id = [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190]
# ds_id = [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190]
# [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]


# updatebv_userstory_datasetable(ds_id)
# plot_histogram_bv(ds_id)
# calculate_bv_dist(ds_id)
# frequency_bv_eachds(ds_id)
# calculate_bv_dist_byrelease(ds_id)
# frequency_bv_byrelease(ds_id)

matching_testcases(ds_id,"1_2","1_3")
# trial(320, "1_","0")

# printres_fromdb(301, ["1","1_2","1_3","0"])