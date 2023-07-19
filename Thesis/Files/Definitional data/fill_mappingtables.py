import random

import mysql.connector
import configparser
import utilities_dataset as ut_ds
import utilities as ut
from datetime import datetime
# import fill_primarytables as currid

config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect = config['dbconnection_dataset']
configuration = config['configuration']
data = config['data']
run_config = config['run_configuration']
tablenames_config = config['tablenames']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)


dataset_tablename = tablenames_config["dataset_tablename"]
usdataset_tablename = tablenames_config["usdatasettable_tablename"]
tcdataset_tablename = tablenames_config["tcdatasettable_tablename"]
defectdataset_tablename = tablenames_config["defectdatasettable_tablename"]

rel1 = data['release1'].split(',')
rel2 = data['release2'].split(',')
uscount_r1 = 10
uscount_r2 = 10
tc_count = int(data['tc_totalcount'])
defect_count = int(data['defect_totalcount'])
usselection_config = "random"   #random or serialized
# tablecreation_config = configuration['tablecreate_config']

config_type = run_config['run_config']
if config_type == "new":
  curr_id = ut_ds.getds_id()
  if curr_id is None:
    next_id = 1
  else:
    next_id = int(curr_id)+1
  current_datetime = datetime.now()
  formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  cols=["ds_id", "run_config", "timestamp"]
  vals = [next_id, config_type, formatted_datetime]
  datatype = ["str", "str", "str"]
  query = ut_ds.insertquery_creation(dataset_tablename, cols, vals, datatype)
  ut_ds.running_insertquery(query)
  print("Finished insert query")

elif config_type == "old":
  config_copiedfrom = run_config["config_copiedfrom"]

else:
  print(f"Wrong input for config_type == {config_type}")

def fillinsttable_usstory():
  usr1count_flag = 0
  usr2count_flag = 0
  cols = ['ds_id', 'us_id', 'us_desc', 'release_id', 'us_points', 'us_businessvalue']
  dtype = ['str', 'int', 'str', 'int', 'int', 'int']
  query_usid = "select us_id, us_desc from userstory;"
  query_releaseid = "select release_id from release_data"
  query_usp = "select us_points,us_businessvalue from userstoryvalue"
  usid_res = ut.running_searchqury(query_usid)
  relid_res = ut.running_searchqury(query_releaseid)
  usv_res = ut.running_searchqury(query_usp)
  usdesclist_rel1 = []
  usdesclist_rel12 = []

  usid_list = ut.createlist_fromdbresult(usid_res,0)
  usdesc_list = ut.createlist_fromdbresult(usid_res,1)
  relid_list = ut.createlist_fromdbresult(relid_res,0)
  usp_list = ut.createlist_fromdbresult(usv_res,0)
  usbv_list = ut.createlist_fromdbresult(usv_res, 1)

  uslist_rel1 = random.sample(usid_res,uscount_r1)

  for i in uslist_rel1:
    if i in usid_res:
      usid_res.remove(i)

  uslist_rel2 = random.sample(usid_res,uscount_r2)
  usidlist_rel1 = ut.createlist_fromdbresult(uslist_rel1,0)
  usdesclist_rel1 = ut.createlist_fromdbresult(uslist_rel1,1)
  usidlist_rel2 = ut.createlist_fromdbresult(uslist_rel2, 0)
  usdesclist_rel2 = ut.createlist_fromdbresult(uslist_rel2, 1)

  usvlist_rel1 = random.sample(usv_res, uscount_r1)

  for i in usvlist_rel1:
    if i in usv_res:
      usv_res.remove(i)

  usvlist_rel2 = random.sample(usv_res, uscount_r2)
  usplist_rel1 = ut.createlist_fromdbresult(usvlist_rel1, 0)
  usbvlist_rel1 = ut.createlist_fromdbresult(usvlist_rel1, 1)
  usplist_rel2 = ut.createlist_fromdbresult(usvlist_rel2, 0)
  usbvlist_rel2 = ut.createlist_fromdbresult(usvlist_rel2, 1)

  insertingvalue_usinsttable(usidlist_rel1, usdesclist_rel1, rel1, usplist_rel1, usbvlist_rel1, usdataset_tablename, cols, dtype)
  insertingvalue_usinsttable(usidlist_rel2, usdesclist_rel2, rel2, usplist_rel2, usbvlist_rel2, usdataset_tablename, cols, dtype)


def insertingvalue_usinsttable(usidlist, usdesclist, relid, usplist, usbvlist, tablename, cols, dtype):

  for ind, i in enumerate(usidlist):
    usid_val = i
    usdesc_val = usdesclist[ind]
    relid_val = int(random.choice(relid))
    usp_val = usplist[ind]
    usbv_val = usbvlist[ind]

    vals = [next_id, usid_val, usdesc_val, relid_val, usp_val, usbv_val]
    query = ut_ds.insertquery_creation(tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut_ds.running_insertquery(query)


def fillinsttable_testcase():
  cols = ['ds_id', 'tc_id', 'tc_executiontime', 'tc_setuptime', 'tc_teardowntime', 'tc_additionalres']
  dtype = ['str', 'str', 'int', 'int', 'int', 'int']
  query_tcid = "select tc_id from testcase"
  query_tcexecutiontime = "select tc_executiontime, tc_setup, tc_teardown, tc_additionalres from tcexectime"
  tcid_res = ut.running_searchqury(query_tcid)
  tcid_list = ut.createlist_fromdbresult(tcid_res, 0)
  tcidlist_total = random.sample(tcid_list, tc_count)

  tcexectime_res = ut.running_searchqury(query_tcexecutiontime)
  tcexectimelist_total = random.sample(tcexectime_res, tc_count)
  tcexectime_list = ut.createlist_fromdbresult(tcexectimelist_total, 0)
  tcsetuptime_list = ut.createlist_fromdbresult(tcexectimelist_total, 1)
  tcteardowntime_list = ut.createlist_fromdbresult(tcexectimelist_total, 2)
  tcaddrestime_list = ut.createlist_fromdbresult(tcexectimelist_total, 3)

  insertingvalue_tcinsttable(tcid_list, tcexectime_list, tcsetuptime_list, tcteardowntime_list, tcaddrestime_list, tcdataset_tablename, cols, dtype)


def insertingvalue_tcinsttable(tcidlist, tcexectime_list, tcsetuptime_list, tcteardowntime_list, tcaddrestime_list, tablename, cols, dtype):

  for ind, i in enumerate(tcidlist):
    tcid_val = i
    tcexectime_val = tcexectime_list[ind]
    tcsetuptime_val = tcsetuptime_list[ind]
    tcteardowntime_val = tcteardowntime_list[ind]
    tcaddrestime_val = tcaddrestime_list[ind]

    vals = [next_id, tcid_val, tcexectime_val, tcsetuptime_val, tcteardowntime_val, tcaddrestime_val]
    query = ut_ds.insertquery_creation(tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut_ds.running_insertquery(query)

def fillinsttable_defectinsttable():
  cols = ['ds_id', 'defect_id', 'defect_severity_id', 'defect_priority_id', 'defect_complexity_id']
  dtype = ['str', 'str', 'int', 'int', 'int']
  defectid_query = "select defect_id from defect"
  defsevid_query = "select defect_severity_id from defect_severity"
  defpriid_query = "select defect_priority_id from defect_priority"
  defcomid_query = "select defect_complexity_id from defect_complexity"

  defid_res = ut.running_searchqury(defectid_query)
  defid_list = ut.createlist_fromdbresult(defid_res, 0)
  defidlist_total = random.sample(defid_list, defect_count)

  defsevid_res = ut.running_searchqury(defsevid_query)
  defsevid_list = ut.createlist_fromdbresult(defsevid_res, 0)

  defpriid_res = ut.running_searchqury(defpriid_query)
  defpriid_list = ut.createlist_fromdbresult(defpriid_res, 0)

  defcomid_res = ut.running_searchqury(defcomid_query)
  defcomid_list = ut.createlist_fromdbresult(defcomid_res, 0)

  insertingvalue_definsttable(defid_list, defsevid_list, defpriid_list, defcomid_list, defectdataset_tablename, cols, dtype)

def insertingvalue_definsttable(defid_list, defsev_list, defpri_list, defcom_list, tablename, cols, dtype):
  for ind, i in enumerate(defid_list):
    defid_val = i
    defsevid_val = random.choice(defsev_list)
    defpri_val = random.choice(defpri_list)
    defcom_val = random.choice(defcom_list)

    vals = [next_id, defid_val, defsevid_val, defpri_val, defcom_val]
    query = ut_ds.insertquery_creation(tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut_ds.running_insertquery(query)

# fillinsttable_usstory()
# fillinsttable_testcase()
fillinsttable_defectinsttable()
