import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
from datetime import datetime
import pandas as pd
import matrixcreation as matc


filepath= "/Thesis/Files/Extra/Database Creation/Mapping.xlsx"
df = pd.read_excel(filepath)
workbook = op.load_workbook(filepath)
config = configparser.ConfigParser()
config.read('config.ini')
dbconnect = config['dbconnection']
configure = config['configuration']
dataconfig = config['data']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

mydb.start_transaction()

# Global Variables
next_id = 0
us_tablename = "user_story"
tc_tablename = "testcase"
defect_tablename = "defect"
sheetname_R1 = "R1"
sheetname_R2 = "R2"
tc_count = matc.total_tccount
total_uscount = 10
total_tccount = 20
connection_prob = 1   # Using a value less than 1 will decrease the 1s even more, so use it wisely
limiting_ones = 8
tcexecutiontime_worksheetname = "TC_Executiontime"
adj_matrix = []
total_tccount = dataconfig["tc_totalcount"]
total_defectcount = dataconfig["defect_totalcount"]
defect_prefix = dataconfig["defect_prefix"]


config_type = configure['tablecreate_config']
if config_type == "new":
  curr_id = ut.gettrack_id()
  if curr_id is None:
    next_id = 1
  else:
    next_id = int(curr_id)+1
  comments = configure["comments"]
  current_datetime = datetime.now()
  formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  cols=["id", "comments", "timestamp"]
  vals = [next_id, comments, formatted_datetime]
  datatype = ["int", "str", "str"]
  query = ut.insertquery_creation("idtracker", cols, vals, datatype)
  ut.running_insertquery(query)
  print("Finished insert query")



def filltable_userstory(sheetname):
  cols = ['us_id', 'us_desc', 'us_points', 'release_id', 'track_id']
  dtype = ['str', 'str', 'int', 'int', 'int']

  df1 = pd.read_excel(filepath, sheet_name=sheetname)
  for _, row in df1.iterrows():
    raw_usid_val = row['US Number']
    usdesc_val = row['User story description']
    usp_val = row['User story points']
    release_val = row['Release']
    usid_val = "R"+str(release_val)+"_"+str(raw_usid_val)
    vals = [usid_val, usdesc_val, usp_val, release_val, next_id]
    query = ut.insertquery_creation(us_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


def filltable_testcase():
  tcexectime_dict = ut.createdictfromexcel(filepath, tcexecutiontime_worksheetname, 1, 2)
  cols = ['tc_id', 'tc_desc', 'tc_executiontime', 'track_id']
  dtype = ['str', 'str', 'int', 'int']

  for key in tcexectime_dict:
    id_val = key
    tcdesc_val = ""
    tc_exectime_val = tcexectime_dict[key]
    track_id = next_id
    vals = [id_val, tcdesc_val, tc_exectime_val, track_id]
    query = ut.insertquery_creation(tc_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)

def filltable_defects():
  cols = ['defect_id', 'defect_desc', 'track_id']
  dtype = ['str', 'str', 'int']
  print(f"type : {type(total_defectcount)}")
  for i in range(int(total_defectcount)):
    id_val = defect_prefix + str(i+1)
    defect_desc = ""
    track_id = next_id
    vals = [id_val, defect_desc, track_id]
    query = ut.insertquery_creation(defect_tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)





filltable_userstory(sheetname_R1)
filltable_userstory(sheetname_R2)
filltable_testcase()
filltable_defects()
