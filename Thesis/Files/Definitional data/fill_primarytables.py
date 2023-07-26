import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
from datetime import datetime
import pandas as pd
import matrixcreation as matc


filepath="C:/Users/amondal8/PycharmProjects/pythonProject3/Thesis/Files/Database Creation/Mapping.xlsx"
df = pd.read_excel(filepath)
workbook = op.load_workbook(filepath)
config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect = config['dbconnection']
dataconfig = config['data']
tablename = config['tablenames']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

mydb.start_transaction()

# Global Variables
next_id = 0
us_tablename = tablename["us_tablename"]
usvalue_tablename = tablename["usvalue_tablename"]
releasedata_tablename = tablename["releasedata"]
sprintdata_tablename = tablename["sprintdata"]
tc_tablename = tablename["tc_tablename"]
tcexectime_tablename = tablename["tcexectime_tablename"]
tcexecstatus_tablename = tablename["tcrunstatus_tablename"]
defect_tablename = tablename["defect_tablename"]
defectcomplexity_tablename = tablename["defectcomplexity_tablename"]
defectpriority_tablename = tablename["defectpriority_tablename"]
defectseverity_tablename = tablename["defectseverity_tablename"]
codemodule_tablename = tablename["codemodule_tablename"]

sheetname_R1 = "R1"
sheetname_R2 = "R2"
sheetname_releasedata = "Release"
sheetname_sprintdata = "Sprint"
tc_count = matc.total_tccount
# connection_prob = 1   # Using a value less than 1 will decrease the 1s even more, so use it wisely
# limiting_ones = 8
tcexecutiontime_worksheetname = "TC_Executiontime"
cm_worksheetname = "Code_module"
adj_matrix = []
total_defectcount_primarytable = 190
defect_prefix = dataconfig["defect_prefix"]


def filltable_userstory(sheetname):
  cols = ['us_id', 'us_desc', 'project_id']
  dtype = ['str', 'str', 'str']

  df1 = pd.read_excel(filepath, sheet_name=sheetname)
  for _, row in df1.iterrows():
    raw_usid_val = row['US Number']
    usdesc_val = row['User story description']
    projectid_val = row['Project_id']
    vals = [raw_usid_val, usdesc_val, projectid_val]
    query = ut.insertquery_creation(us_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_userstorypoints(sheetname):
  cols = ['us_points']
  dtype = ['int']

  df1 = pd.read_excel(filepath, sheet_name=sheetname)
  for _, row in df1.iterrows():
    usp_val = row['User story points']
    vals = [usp_val]
    query = ut.insertquery_creation(usvalue_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)

def filltable_testcase(sheetname):
  # tcexectime_dict = ut.createdictfromexcel(filepath, tcexecutiontime_worksheetname, 1, 2)
  cols = ['tc_id']
  dtype = ['str']

  df1 = pd.read_excel(filepath, sheet_name=sheetname)
  for _, row in df1.iterrows():
    tcid_val = row['tc_id']
    vals = [tcid_val]
    query = ut.insertquery_creation(tc_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)

def filltable_defects():
  cols = ['defect_id']
  dtype = ['str']
  # print(f"type : {type(total_defectcount)}")
  for i in range(int(total_defectcount_primarytable)):
    id_val = defect_prefix + str(i+1)
    vals = [id_val]
    query = ut.insertquery_creation(defect_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)

def filltable_tcrunstatus():
  cols = ['status_id', 'status_desc']
  dtype = ['int', 'str']
  statusid_vals = [1,2,3,4,5,6,7]
  statusdesc_vals = ["Passed","Failed","Not Run","Deferred","Skipped","Blocked","Not Applicable"]
  for ind, i in enumerate(statusid_vals):
    status_id = i
    status_desc = statusdesc_vals[ind]
    vals = [status_id, status_desc]
    query = ut.insertquery_creation(tcexecstatus_tablename, cols, vals, dtype)
    # print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_defectpriority():
  cols = ['defect_priority_id', 'defect_priority_desc']
  dtype = ['int', 'str']
  statusid_vals = [1,2,3,4]
  statusdesc_vals = ["Low","Medium","High","Critical"]
  for ind, i in enumerate(statusid_vals):
    status_id = i
    status_desc = statusdesc_vals[ind]
    vals = [status_id, status_desc]
    query = ut.insertquery_creation(defectpriority_tablename, cols, vals, dtype)
    # print(f"query is : {query}")
    ut.running_insertquery(query)

def filltable_defectseverity():
  cols = ['defect_severity_id', 'defect_severity_desc']
  dtype = ['int', 'str']
  statusid_vals = [1,2,3,4]
  statusdesc_vals = ["Cosmetic","Minor","Major","Critical"]
  for ind, i in enumerate(statusid_vals):
    status_id = i
    status_desc = statusdesc_vals[ind]
    vals = [status_id, status_desc]
    query = ut.insertquery_creation(defectseverity_tablename, cols, vals, dtype)
    # print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_defectcomplexity():
  cols = ['defect_complexity_id', 'defect_complexity_desc']
  dtype = ['int', 'str']
  statusid_vals = [1,2,3,4]
  statusdesc_vals = ["Low","Medium","High","Very High"]
  for ind, i in enumerate(statusid_vals):
    status_id = i
    status_desc = statusdesc_vals[ind]
    vals = [status_id, status_desc]
    query = ut.insertquery_creation(defectcomplexity_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_releasedata(sheetname):
  cols = ["release_id"]
  dtype = ["str"]

  df1 = pd.read_excel(filepath, sheet_name = sheetname)
  for _, row in df1.iterrows():
    raw_usid_val = row['release_id']
    # start_date = row['start_date']
    # end_date = row['end_date']
    vals = [raw_usid_val]
    query = ut.insertquery_creation(releasedata_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_sprintdata(sheetname):
  cols = ["sprint_id"]
  dtype = ["str"]

  df1 = pd.read_excel(filepath, sheet_name = sheetname)
  for _, row in df1.iterrows():
    raw_usid_val = row['sprint_id']
    # start_date = row['start_date']
    # end_date = row['end_date']
    vals = [raw_usid_val]
    query = ut.insertquery_creation(sprintdata_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_tcexecutiontime(sheetname):
  cols = ["tc_executiontime", "tc_setup", "tc_teardown", "tc_additionalres"]
  dtype = ["int", "int", "int", "int"]

  df1 = pd.read_excel(filepath, sheet_name = sheetname)
  for _, row in df1.iterrows():
    tcexectime_val = row['tc_executiontime']
    tcstartuptime_val = row['tc_setup']
    tcteardowntime_val = row['tc_teardown']
    tcaddrestime_val = row['tc_additionalres']
    vals = [tcexectime_val, tcstartuptime_val, tcteardowntime_val, tcaddrestime_val]
    query = ut.insertquery_creation(tcexectime_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)

def filltable_codemodule(sheetname):
  cols = ['cm_id', 'cm_desc']
  dtype = ['str', 'str']

  df1 = pd.read_excel(filepath, sheet_name=sheetname)
  for _, row in df1.iterrows():
    cmid_val = row['cm_id']
    cm_desc = row['cm_desc']
    vals = [cmid_val, cm_desc]
    query = ut.insertquery_creation(codemodule_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


filltable_userstory(sheetname_R1)
filltable_userstory(sheetname_R2)

filltable_userstorypoints(sheetname_R1)
filltable_userstorypoints(sheetname_R2)
filltable_releasedata(sheetname_releasedata)
filltable_sprintdata(sheetname_sprintdata)
filltable_testcase(tcexecutiontime_worksheetname)
filltable_defects()
filltable_tcrunstatus()
filltable_defectpriority()
filltable_defectseverity()
filltable_defectcomplexity()
filltable_tcexecutiontime(tcexecutiontime_worksheetname)
filltable_codemodule(cm_worksheetname)
