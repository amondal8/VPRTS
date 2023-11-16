import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
from datetime import datetime
import pandas as pd
import matrixcreation as matc
import defectmapping as defmap
import contextualComparison_final as contcomp
import creatingsubsets as createsubset

filepath = "/Thesis/Files/Extra/Database Creation/Mapping.xlsx"
config = configparser.ConfigParser()
config.read('config.ini')
dbconnect = config['dbconnection']
configure = config['configuration']
dataconfig = config['data']
fixedvarconfig = config['fixedvariables']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

mydb.start_transaction()

# Global Variables
us_tablename = fixedvarconfig["us_tablename"]
tc_tablename = fixedvarconfig["tc_tablename"]
defect_tablename = fixedvarconfig["defect_tablename"]
ustcmap_tablename = fixedvarconfig["ustcmap_tablename"]
tcdefectmap_tablename = fixedvarconfig["tcdefectmap_tablename"]
sheetname_R1 = "R1"
sheetname_R2 = "R2"
total_uscount = int(dataconfig["us_totalcount"])
total_tccount = int(dataconfig["tc_totalcount"])
total_defectcount = int(dataconfig["defect_totalcount"])
tc_prefix = dataconfig["tc_prefix"]
defect_prefix = dataconfig["defect_prefix"]
usp_threshold = int(dataconfig["usp_threshold"])
tc_list = []
total_exectime = 90
tc_exectime = 15
worksheetname_executiontime = "TC_Executiontime"

next_id = ut.gettrack_id()


# Configuration is the  way we want to calculate the cumulative value
# of the user story and how it is carried to the other user stories
# configuration=1        -> when the value of R2 is carried to R1
# configuration=2        -> when the value of R1 is carried to R2
# configuration=3        -> when the value of R1 + R2 is carried and placed beside R1
# configuration=4        -> when the value of R2 is carried to R1 with weight of similarity value being considered

configuration = 3

contcomp.texualcomparison(configuration)
us_list = createsubset.creation_userstorysubsets(usp_threshold)

def creation_tcsubset(us_list):
  query = ut.create_searchquery(us_list, "tc_id", "us_tc_map", "us_id", next_id, "R1_")
  result = ut.running_searchqury(query)
  tc_list = []
  for ind,i in enumerate(result):
    tc_list.append(result[ind][0])
  print(f"Printing the selected set of test cases based on the user story selection: {sorted(tc_list)}")
  print(f"Number of test cases selected = {len(tc_list)} out of a total of {total_tccount} test cases")
  print(f"Selection rate: {(len(tc_list) / total_tccount) * 100}")
  return sorted(tc_list)


def creation_defectsubset(tc_list):
  query = ut.create_searchquery(tc_list, "defect_id", "tc_defect_map", "tc_id", next_id,  "")
  result = ut.running_searchqury(query)
  defect_list = []
  for ind,i in enumerate(result):
    defect_list.append(result[ind][0])
  print(f"Printing the identified set of defects based on the selected subset of test cases: {sorted(defect_list)}")
  print(f"Number of defects identified = {len(defect_list)} out of a total of {total_defectcount} defects")
  return sorted(defect_list)


tc_list = creation_tcsubset(us_list)
sorted_tcdict = ut.creating_prioritydict_tclist(tc_list, next_id)
createsubset.creatingtcset_fixedexecutiontime(sorted_tcdict, total_exectime, tc_exectime)
tcexec_dict = createsubset.createdictfromexcel(filepath, worksheetname_executiontime, 1, 2)  # Creating a dictionary where TC# is the key and its execution time is the value
createsubset.creatingtcset_varyingecutiontime(sorted_tcdict, total_exectime, tcexec_dict)    # Creating a smaller subset of test cases based on the variable exacution time for each test case
defect_list = creation_defectsubset(tc_list)
