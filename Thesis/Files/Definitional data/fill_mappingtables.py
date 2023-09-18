import random

import mysql.connector
import configparser
import utilities_dataset as ut_ds
import utilities as ut
from datetime import datetime
import matrixcreation as matc
import defectmapping as defmap

inifilename_stored = "inifile_name.txt"
config = configparser.ConfigParser()
configfilename = ut.read_from_txt(inifilename_stored)
config.read(configfilename)
dbconnect = config['dbconnection_dataset']
data = config['data']
run_config = config['run_configuration']
tablenames_config = config['tablenames']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

rel1 = data['release1']
rel2 = data['release2']
us_count = int(data['us_totalcount'])
uscount_r1 = int(data["uscount_r1"])
tc_count = int(data['tc_totalcount'])
cm_count = int(data["cm_totalcount"])
limiting_ones = int(data['limiting_ones'])
defect_count = int(data['defect_totalcount'])
tcdefect_map_probthreshold = float(data['tcdefect_map_probthreshold'])
uscm_map_probthreshold = float(data['uscm_map_probthreshold'])
ustcmap_tablename = tablenames_config["ustcmap_tablename"]
uscmmap_tablename = tablenames_config["uscmmap_tablename"]
tcdefectmap_tablename = tablenames_config["tcdefectmap_tablename"]
matrix_build_config_uscm = run_config["matrix_build_config_uscm"]
matrix_build_config_tcdefect = run_config["matrix_build_config_tcdefect"]
matrix_build_configtype_ustc = run_config["matrix_build_configtype_ustc"]
copy_ds_id = run_config["copy_ds_id"]
run_conf = run_config["run_config"]
next_id = ut_ds.getds_id()
# next_id = "21"
if copy_ds_id.lower() == "yes" and run_conf.lower() == "copy":
    copied_dsid = run_config["config_copiedfrom"]
    print(f"config_copiedfrom: {copied_dsid}")
    ds_id = copied_dsid
else:
    ds_id = ut_ds.getds_id()


print(f"matrix_build_config_tcdefect: {matrix_build_config_tcdefect}")


def runningmats():
    print(f"uscount: {uscount_r1} and tccount: {tc_count}")
    adj_matrixtcmap = matc.generate_adjmat_onetomany_withlimits(uscount_r1, tc_count, limiting_ones, connection_probability=.3)
    if matrix_build_config_tcdefect.lower() == "even":
        adj_matrixdefectmap = defmap.generate_defectmap_adjmat_withlimits(tc_count, defect_count, connection_prob=.5, lower_limitones=0, upper_limitones=4)
    elif matrix_build_config_tcdefect.lower() == "composite":
        matrix_build_configtype_tcdefect = run_config["matrix_build_configtype_tcdefect"]
        adj_matrixdefectmap = matc.generate_custom_adjacency_matrix(tc_count,defect_count,tcdefect_map_probthreshold,matrix_build_configtype_tcdefect)

    return adj_matrixtcmap, adj_matrixdefectmap

# print(f"Defect mat is: ")
# for row in adj_matrixdefectmap:
#     print(row)

# matc.writematto_reqmappingexcel(adj_matrixtcmap)
# matc.writeto_revReqMat_excel(adj_matrixtcmap)

def fillmappingtable_ustcmap(adj_matrixtcmap):
    print(f"next_id: {next_id} and ds_id: {ds_id}")
    # print(adj_matrixtcmap)
    cols = ['us_id', 'tc_id', 'ds_id']
    dtype = ['str', 'str', 'str']

    query_usid = f"select us_id from userstory_datasettable where ds_id = {ds_id} and release_id in ({rel1}) "
    query_tcid = f"select tc_id from tc_datasettable where ds_id = {ds_id}"
    # print(query_tcid + '\n' +  query_usid)
    usid_res = ut_ds.running_searchqury(query_usid)
    tcid_res = ut_ds.running_searchqury(query_tcid)

    usid_list = ut.createlist_fromdbresult(usid_res, 0)
    tcid_list = ut.createlist_fromdbresult(tcid_res, 0)
    for i in adj_matrixtcmap:
        print(i)

    for row in range(len(adj_matrixtcmap)):
        ones_list = ut.fetch_ones_in_row(adj_matrixtcmap, row)
        print(f"ones_list: {ones_list}")
        if ones_list is not None:
            for i in ones_list:
                print(f"row:{row} i: {i}")
                print(f"usid_list[row]: {usid_list[row]}, tcid_list[i]: {tcid_list[i]}")
                vals = [usid_list[row], tcid_list[i], next_id]
                query = ut.insertquery_creation(ustcmap_tablename, cols, vals, dtype)
                print(f"query is : {query}")
                ut_ds.running_insertquery(query)
        else:
            continue


def fillmappingtable_tcdefectsmap(adj_matrixdefectmap):
  print(adj_matrixdefectmap)
  cols = ['tc_id', 'defect_id', 'ds_id']
  dtype = ['str', 'str', 'str']

  query_tcid = f"select tc_id from tc_datasettable where ds_id = {ds_id}"
  query_defectid = f"select defect_id from defect_datasettable where ds_id = {ds_id}"

  tcid_res = ut_ds.running_searchqury(query_tcid)
  defectid_res = ut_ds.running_searchqury(query_defectid)


  tcid_list = ut.createlist_fromdbresult(tcid_res, 0)
  defectid_list = ut.createlist_fromdbresult(defectid_res, 0)

  for row in range(len(adj_matrixdefectmap)):
    ones_list = ut.fetch_ones_in_row(adj_matrixdefectmap, row)
    for i in ones_list:
      vals = [tcid_list[row], defectid_list[i], next_id]
      query = ut.insertquery_creation(tcdefectmap_tablename, cols, vals, dtype)
      print(f"query is : {query}")
      ut_ds.running_insertquery(query)


def fillmappingtable_uscmmap():
    cols = ['us_id', 'cm_id', 'affected_value', 'ds_id']
    dtype = ['str', 'str', 'str', 'str']

    query_usid = f"select us_id from userstory_datasettable where ds_id = {ds_id}"
    query_cmid = f"select cm_id from cm_datasettable where ds_id = {ds_id}"
    print(f"query: {query_usid}")
    usid_res = ut_ds.running_searchqury(query_usid)
    usid_list = ut.createlist_fromdbresult(usid_res, 0)
    cmid_res = ut_ds.running_searchqury(query_cmid)
    cmid_list = ut.createlist_fromdbresult(cmid_res, 0)
    print(f"matrix_build_config_uscm: {matrix_build_config_uscm}")

    # print(usid_list)
    if matrix_build_config_uscm.lower() == "even":
        adj_uscmmap = matc.generate_tccmmap_adjmat_withlimits(len(usid_list),len(cmid_list),connection_prob=1,lower_limitones = 1,upper_limitones = 4)
    elif matrix_build_config_uscm.lower() == "composite":
        print("inside composite")
        matrix_build_configtype_uscm = run_config["matrix_build_configtype_uscm"]
        adj_uscmmap = matc.generate_custom_adjacency_matrix_uscm(len(usid_list), len(cmid_list), uscm_map_probthreshold, matrix_build_configtype_uscm)
    print(f"uscm Mat: ")
    # for r in adj_uscmmap:
    #     print(r)
    for row in range(len(adj_uscmmap)):
        nonzero_list = ut.fetch_nonzeros_in_row(adj_uscmmap, row)
        # print(nonzero_list)
        for i in nonzero_list:
            vals = [usid_list[row], cmid_list[i], adj_uscmmap[row][i], next_id]
            query = ut.insertquery_creation(uscmmap_tablename, cols, vals, dtype)
            # print(f"query is : {query}")
            ut_ds.running_insertquery(query)


# adj_matrixtcmap, adj_matrixdefectmap = runningmats()
# for i in adj_matrixtcmap:
#     print(i)



# fillmappingtable_ustcmap(adj_matrixtcmap)
# fillmappingtable_tcdefectsmap(adj_matrixdefectmap)
# fillmappingtable_uscmmap()
# ut.saving_config(configfilename, next_id)




