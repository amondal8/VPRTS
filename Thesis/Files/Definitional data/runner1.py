import time
import utilities as ut
import utilities_dataset as ut_ds
import config_initialsetup as inisetup
import fill_mappingtables as fm


# time.sleep(10)
import fill_datasettables as fd


# writing to excel
colindex = ["next", "same", "same", "same", "same"]
col = ["A", "F", "G", "H", "I"]

#data = [ds_id/next_id, uscount_rel1, uscount_rel2, cmcount, tccount, defectcount, multiplier, addingfactor]
# data = [["33", 60, 75, 40, 400, 70, 3000, 500]]


# ["21", 15, 15, 20, 40, 30, 500, 500],["22", 20, 30, 40, 200, 60, 500, 500], ["23", 25, 25, 40, 100, 60, 1000, 500], ["24", 40, 10, 60, 300, 60, 1000, 500], ["25", 40, 40, 70, 140, 60, 1000, 500], ["26", 30, 50, 70, 350, 60, 1000, 500], ["27", 60, 60, 70, 200, 120, 1000, 500], ["28", 40, 80, 70, 400, 120, 1000, 500], ["29", 75, 75, 70, 250, 130, 1000, 500], ["30", 60, 90, 70, 500, 150, 1000, 500], ["31", 40, 15, 20, 200, 70, 3000, 500], ["32", 50, 15, 20, 300, 70, 4000, 500]


# for indi, i in enumerate(colindex):
#     if indi == 4:
#         ut_ds.writeconfigs_to_excel(colindex[indi], i, data[indi+1])
#     else:
#         ut_ds.writeconfigs_to_excel(colindex[indi], i, data[indi])
def runner1(data):
    for indi, i in enumerate(data):
        print(f"Working on data #{indi}: {i}")
        for indj, j in enumerate(col):
            if indj == 4:
                ut_ds.writeconfigs_to_excel(colindex[indj], j, i[indj+1])
            else:
                ut_ds.writeconfigs_to_excel(colindex[indj], j, i[indj])
        fd.next_id = i[0]
        fd.uscount_r1 = i[1]
        fd.uscount_r2 = i[2]
        fd.cm_count = i[3]
        fd.tc_count = i[4]
        fd.defect_count = i[5]
        inisetup.initimple(i[0])

        fd.fillinsttable_usstory()
        fd.fillinsttable_testcase()
        fd.fillinsttable_cminsttable()
        fd.fillinsttable_defectinsttable()
        fd.insertbusinessvalue(i[6], i[6], i[0])
    #
        ut.saving_config(fd.configfilename, fd.next_id)