import time
import utilities as ut
import config_initialsetup as inisetup
# time.sleep(10)
import fill_datasettables as fd
import fill_mappingtables as fm
import utilities_dataset as ut_ds
# import final_implementation1 as fi

#data = [ds_id/next_id, uscount_rel1, uscount_rel2, cmcount, tccount, defectcount, multiplier, addingfactor]

# data = [["33", 60, 75, 40, 400, 70, 3000, 500]]


# data = [["21", 15, 15, 20, 40, 30, 500, 500],["22", 20, 30, 40, 200, 60, 500, 500],["23", 25, 25, 40, 100, 60, 1000, 500],["24", 40, 10, 60, 300, 60, 1000, 500], ["25", 40, 40, 70, 140, 60, 1000, 500], ["26", 30, 50, 70, 350, 60, 1000, 500], ["27", 60, 60, 70, 200, 120, 1000, 500], ["28", 40, 80, 70, 400, 120, 1000, 500], ["29", 75, 75, 70, 250, 130, 1000, 500], ["30", 60, 90, 70, 500, 150, 1000, 500]]

#
def runner2(data):
    dsid_list = []
    for i in data:
        fm.ds_id = i[0]
        fm.next_id = i[0]
        fm.uscount_r1 = i[1]
        fm.tc_count = i[4]

        adj_matrixtcmap, adj_matrixdefectmap = fm.runningmats()
        fm.fillmappingtable_ustcmap(adj_matrixtcmap)
        fm.fillmappingtable_tcdefectsmap(adj_matrixdefectmap)
        fm.fillmappingtable_uscmmap()
    ut_ds.commitconnection()
    for i in data:
        query = f"select tc_id from us_tc_map where ds_id = '{i[0]}'"
        result = ut_ds.running_searchqury(query)
        print(len(result))
        ut_ds.readandwrite_toexcel(i[0], "D", len(result))
    for i in data:
        dsid_list.append(i[0])
    print(f"dsid_list")

# ut.saving_config(fd.configfilename, fd.next_id)