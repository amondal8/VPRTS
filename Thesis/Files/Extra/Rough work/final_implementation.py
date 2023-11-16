import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
import utilities_dataset as ut_ds
from datetime import datetime
import pandas as pd
import contextualComparison_usingdb as contcomp
import creatingsubsets as createsubset

outputfilename = "output.txt"
inifilename_stored = "inifile_name.txt"
filepath = "/Thesis/Files/Database Creation/Mapping.xlsx"
config = configparser.ConfigParser()
configfilename = ut.read_from_txt(inifilename_stored)
config.read(configfilename)
dbconnect = config['dbconnection_dataset']
data = config['data']
tablenames_config = config['tablenames']
run_config = config['run_configuration']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

mydb.start_transaction()

# Global Variables
dataset_tablename = tablenames_config["dataset_tablename"]
ustcmap_tablename = tablenames_config["ustcmap_tablename"]
uscmmap_tablename = tablenames_config["uscmmap_tablename"]
tcdefectmap_tablename = tablenames_config["tcdefectmap_tablename"]
usp_threshold = int(data["usp_threshold"])
total_tccount = int(data["tc_totalcount"])
total_defectcount = int(data["defect_totalcount"])
total_executiontime = int(data["total_executiontime"])
tcexectime_fixed = int(data["tcexectime_fixed"])
copy_ds_id = run_config["copy_ds_id"]
run_conf = run_config["run_config"]
next_id = ut_ds.getds_id()
# importanceval_calconfig = data["importanceval_calconfig"]
# if importanceval_calconfig not in ["1","2"]:
#   importanceval_calconfig = "1"

importanceval_calconfig = "2"
ds_id_res = ut_ds.getds_id()
tc_list = []
worksheetname_executiontime = "TC_Executiontime"

if(copy_ds_id.lower() == "yes" and run_conf.lower() == "copy"):
  copied_dsid = run_config["config_copiedfrom"]
  print(f"config_copiedfrom: {copied_dsid}")
  ds_id = copied_dsid
else:
  ds_id = ut_ds.getds_id()


# Configuration is the  way we want to calculate the cumulative value
# of the user story and how it is carried to the other user stories
# configuration=1        -> when the value of R2 is carried to R1
# configuration=2        -> when the value of R1 is carried to R2
# configuration=3        -> when the value of R1 + R2 is carried and placed beside R1 multiplied with cm val
# configuration=4        -> when the value of R2 is carried to R1 with weight of similarity value being considered


us_dict = ut.copy_console('w', contcomp.contentcomparison, ds_id, importanceval_calconfig)
us_list = ut.copy_console('a', createsubset.creation_userstorysubsets, us_dict, usp_threshold)    #usp_threshold can be changed from config file

print(f"us_list: {us_list}")

def creation_tcsubset(us_list):
  query = ut.create_searchquery(us_list, "tc_id", ustcmap_tablename, "us_id", ds_id, "")
  result = ut_ds.running_searchqury(query)
  tc_list = []
  for ind,i in enumerate(result):
    tc_list.append(result[ind][0])
  print(f"Printing the selected set of test cases based on the user story selection: {sorted(tc_list)}")
  print(f"Number of test cases selected = {len(tc_list)} out of a total of {total_tccount} test cases")
  print(f"Selection rate: {(len(tc_list) / total_tccount) * 100}")
  return sorted(tc_list)


def creation_defectsubset(tc_list):
  query = ut.create_searchquery(tc_list, "defect_id", tcdefectmap_tablename, "tc_id", ds_id,  "")
  result = ut_ds.running_searchqury(query)
  defect_list = []
  for ind,i in enumerate(result):
    defect_list.append(result[ind][0])
  print(f"Printing the identified set of defects based on the selected subset of test cases: {sorted(defect_list)}")
  print(f"Number of defects identified = {len(defect_list)} out of a total of {total_defectcount} defects")
  return sorted(defect_list)


def saving_results():
  result_text = ut.read_from_txt(outputfilename)
  print(f"filename: {outputfilename}")
  query_updateresults = ut.updatetable_query(dataset_tablename, "results", result_text, "str", ds_id_res)
  ut_ds.running_insertquery(query_updateresults)

def saving_config():
  json_data = ut_ds.ini_to_json(configfilename)
  ut_ds.insert_json_data(json_data, ds_id_res)

tc_list = ut.copy_console('a', creation_tcsubset, us_list)
print(f"tc_list:{tc_list}")
sorted_tcdict = ut.copy_console('a',ut_ds.creating_prioritydict_tclist,tc_list, ds_id)
ut.copy_console('a', createsubset.creatingtcset_fixedexecutiontime, sorted_tcdict, total_executiontime, tcexectime_fixed)
tcexec_dict = ut.copy_console('a', createsubset.create_tcdict_exectime, tc_list, ds_id)  # Creating a dictionary where TC# is the key and its execution time is the value
print(f"sorted_tcdict {sorted_tcdict}")
print(f"tcexec_dict {tcexec_dict}")
ut.copy_console('a', createsubset.creatingtcset_varyingecutiontime, sorted_tcdict, total_executiontime, tcexec_dict)    # Creating a smaller subset of test cases based on the variable exacution time for each test case
defect_list = ut.copy_console('a', creation_defectsubset, tc_list)
# saving_results()
# ut.saving_config(configfilename, next_id)

