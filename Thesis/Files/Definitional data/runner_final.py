import utilities_dataset as ut_ds
import time
import runner1 as r1
import runner2 as r2
import data as dt

dsid_list = []

# data = [["34", 100, 50, 40, 500, 70, 1000, 500], ["35", 50, 100, 40, 300, 70, 1000, 500], ["36", 10, 50, 40, 100, 70, 1000, 500], ["37", 20, 35, 40, 200, 70, 1000, 500], ["38", 10, 50, 40, 100, 70, 1000, 500], ["39", 50, 50, 40, 400, 70, 2000, 500], ["40",30, 10, 40, 300, 70, 3000, 500]]
# ["33", 60, 75, 40, 400, 70, 3000, 500]

data = dt.data

r1.runner1(data)
ut_ds.commitconnection()
r2.runner2(data)
ut_ds.commitconnection()

for i in data:
    dsid_list.append(i[0])

print(f"dsid_list: {dsid_list}")