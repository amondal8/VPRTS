import random

import mysql.connector
import configparser
import utilities_dataset as ut_ds
import utilities as ut
from datetime import datetime
import matrixcreation as matc
import defectmapping as defmap

config = configparser.ConfigParser()
config.read('config1.ini')
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
us_count = int(data['us_totalcount'])
uscount_r1 = int(data["uscount_r1"])
tc_count = int(data['tc_totalcount'])
cm_count = int(data["cm_totalcount"])
limiting_ones = int(data['limiting_ones'])
defect_count = int(data['defect_totalcount'])
ustcmap_tablename = tablenames_config["ustcmap_tablename"]
uscmmap_tablename = tablenames_config["uscmmap_tablename"]
tcdefectmap_tablename = tablenames_config["tcdefectmap_tablename"]
ds_id = ut_ds.getds_id()

adj_matrixtcmap = matc.generate_adjmat_onetomany_withlimits(uscount_r1, tc_count, limiting_ones, connection_probability=.5)
adj_matrixdefectmap = defmap.generate_defectmap_adjmat_withlimits(tc_count, defect_count, connection_prob=1, lower_limitones=0, upper_limitones=4)
for row in adj_matrixtcmap:
    print(row)

# matc.writematto_reqmappingexcel(adj_matrixtcmap)
# matc.writeto_revReqMat_excel(adj_matrixtcmap)

def fillmappingtable_ustcmap():
    # print(adj_matrixtcmap)
    cols = ['us_id', 'tc_id', 'ds_id']
    dtype = ['str', 'str', 'str']

    query_usid = f"select us_id from userstory_datasettable where ds_id = {ds_id} and release_id in ({rel1}) "
    query_tcid = f"select tc_id from tc_datasettable where ds_id = {ds_id}"
    usid_res = ut_ds.running_searchqury(query_usid)
    tcid_res = ut_ds.running_searchqury(query_tcid)

    usid_list = ut.createlist_fromdbresult(usid_res, 0)
    tcid_list = ut.createlist_fromdbresult(tcid_res, 0)


    for row in range(len(adj_matrixtcmap)):
        ones_list = ut.fetch_ones_in_row(adj_matrixtcmap, row)
        for i in ones_list:
            # print(f"row:{row} i: {i}")
            vals = [usid_list[row], tcid_list[i], ds_id]
            query = ut.insertquery_creation(ustcmap_tablename, cols, vals, dtype)
            print(f"query is : {query}")
            ut_ds.running_insertquery(query)


def fillmappingtable_tcdefectsmap():
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
      vals = [tcid_list[row], defectid_list[i], ds_id]
      query = ut.insertquery_creation(tcdefectmap_tablename, cols, vals, dtype)
      print(f"query is : {query}")
      ut_ds.running_insertquery(query)


def fillmappingtable_uscmmap():
    cols = ['us_id', 'cm_id', 'affected_value', 'ds_id']
    dtype = ['str', 'str', 'str', 'str']

    query_usid = f"select us_id from userstory_datasettable where ds_id = {ds_id} and release_id in ({rel1})"
    query_cmid = f"select cm_id from cm_datasettable where ds_id = {ds_id} and release_id in ({rel1})"
    print(f"query: {query_usid}")
    usid_res = ut_ds.running_searchqury(query_usid)
    usid_list = ut.createlist_fromdbresult(usid_res, 0)
    cmid_res = ut_ds.running_searchqury(query_cmid)
    cmid_list = ut.createlist_fromdbresult(cmid_res, 0)

    print(usid_list)
    adj_uscmmap = matc.generate_tccmmap_adjmat_withlimits(len(usid_list),len(cmid_list),connection_prob=1,lower_limitones = 1,upper_limitones = 4)

    for row in range(len(adj_uscmmap)):
        nonzero_list = ut.fetch_nonzeros_in_row(adj_uscmmap, row)
        print(nonzero_list)
        for i in nonzero_list:
            vals = [usid_list[row], cmid_list[i], adj_uscmmap[row][i], ds_id]
            query = ut.insertquery_creation(uscmmap_tablename, cols, vals, dtype)
            print(f"query is : {query}")
            ut_ds.running_insertquery(query)


fillmappingtable_ustcmap()
fillmappingtable_tcdefectsmap()
fillmappingtable_uscmmap()




