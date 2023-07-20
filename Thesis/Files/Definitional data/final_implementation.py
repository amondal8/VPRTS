import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
import utilities_dataset as ut_ds
from datetime import datetime
import pandas as pd
import contextualComparison_usingdb as contcomp
import creatingsubsets as createsubset

filepath = "C:/Users/amondal8/PycharmProjects/pythonProject3/Thesis/Files/Database Creation/Mapping.xlsx"
config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect = config['dbconnection_dataset']
data = config['data']
tablenames_config = config['tablenames']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

mydb.start_transaction()

# Global Variables
ustcmap_tablename = tablenames_config["ustcmap_tablename"]
uscmmap_tablename = tablenames_config["uscmmap_tablename"]
tcdefectmap_tablename = tablenames_config["tcdefectmap_tablename"]
usp_threshold = int(data["usp_threshold"])
total_tccount = int(data["tc_totalcount"])
total_defectcount = int(data["defect_totalcount"])
total_executiontime = int(data["total_executiontime"])
tcexectime_fixed = int(data["tcexectime_fixed"])



sheetname_R1 = "R1"
sheetname_R2 = "R2"
# total_uscount = int(dataconfig["us_totalcount"])
# total_tccount = int(dataconfig["tc_totalcount"])
# total_defectcount = int(dataconfig["defect_totalcount"])
# tc_prefix = dataconfig["tc_prefix"]
# defect_prefix = dataconfig["defect_prefix"]
tc_list = []
total_exectime = 90
tc_exectime = 15
worksheetname_executiontime = "TC_Executiontime"

ds_id = ut_ds.getds_id()


# Configuration is the  way we want to calculate the cumulative value
# of the user story and how it is carried to the other user stories
# configuration=1        -> when the value of R2 is carried to R1
# configuration=2        -> when the value of R1 is carried to R2
# configuration=3        -> when the value of R1 + R2 is carried and placed beside R1
# configuration=4        -> when the value of R2 is carried to R1 with weight of similarity value being considered

configuration = 3

# contcomp.texualcomparison(configuration)
us_dict = contcomp.contentcomparison(ds_id)
us_list = createsubset.creation_userstorysubsets(us_dict, usp_threshold)

print(us_list)

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


def read_ini_as_blob(file_path):
  with open(file_path, 'rb') as file:
    blob_data = file.read()
  return blob_data


def saving_configuration():
  ini_filepath = "C:\\Users\\amondal8\\PycharmProjects\\pythonProject3\\Thesis\\Files\\Definitional data\\config1.ini"
  blob_data = read_ini_as_blob(ini_filepath)
  # query = f"Insert into dataset(ini_file) Values ({blob_data}) where ds_id = {ds_id}"
  # ut_ds.running_insertquery(query)

  print(blob_data)

# tc_list = creation_tcsubset(us_list)
# sorted_tcdict = ut_ds.creating_prioritydict_tclist(tc_list, ds_id)
# createsubset.creatingtcset_fixedexecutiontime(sorted_tcdict, total_executiontime, tcexectime_fixed)
# tcexec_dict = createsubset.create_tcdict_exectime(tc_list, ds_id)  # Creating a dictionary where TC# is the key and its execution time is the value
# print(f"sorted_tcdict {sorted_tcdict}")
# print(f"tcexec_dict {tcexec_dict}")
# createsubset.creatingtcset_varyingecutiontime(sorted_tcdict, total_exectime, tcexec_dict)    # Creating a smaller subset of test cases based on the variable exacution time for each test case
# defect_list = creation_defectsubset(tc_list)
saving_configuration()