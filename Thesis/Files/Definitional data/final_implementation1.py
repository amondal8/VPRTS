import random

import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
import utilities_dataset as ut_ds
from datetime import datetime
import pandas as pd
import contextualComparison_usingdb as contcomp
import creatingsubsets as createsubset
import data as dt

outputfilename = "output.txt"
inifilename_stored = "inifile_name.txt"

#Add your credentials/path
filepath = "/Thesis/Files/Extra/Database Creation/Mapping.xlsx"

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
valuepreserved_col = ""
importanceval_calconfig = dt.importanceval_calconfig
#
dsid_list = dt.dsid_list

# [256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340]
# 142, 143, 144, 145, 146, 147, 148, 149, 150, 151,152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190
  # [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]
total_executiontime_list = dt.exec_window


# ,"1.2","1.3","0"
# ds_id_res = ut_ds.getds_id()
# ds_id_res = ds_id = "22"
worksheetname_executiontime = "TC_Executiontime"

# if(copy_ds_id.lower() == "yes" and run_conf.lower() == "copy"):
#   copied_dsid = run_config["config_copiedfrom"]
#   print(f"config_copiedfrom: {copied_dsid}")
#   ds_id = copied_dsid
# else:
#   ds_id = ut_ds.getds_id()




# Configuration is the  way we want to calculate the cumulative value
# of the user story and how it is carried to the other user stories
# configuration=1        -> when the value of R2 is carried to R1
# configuration=2        -> when the value of R1 is carried to R2
# configuration=3        -> when the value of R1 + R2 is carried and placed beside R1 multiplied with cm val
# configuration=4        -> when the value of R2 is carried to R1 with weight of similarity value being considered

def get_usdict(ds_id, importanceval_calconfig):
  us_dict = ut.copy_console('w', contcomp.contentcomparison, ds_id, importanceval_calconfig)
  return us_dict
# us_list = ut.copy_console('a', createsubset.creation_userstorysubsets, us_dict, usp_threshold)    #usp_threshold can be changed from config file

# print(f"us_dict: {us_dict}")

def creation_tcsubset(us_dict, ds_id):
  tc_dict = {}
  for key in us_dict:
    # print(key)
    query = f"select tc_id from us_tc_map where us_id = {key} and ds_id = '{ds_id}'"
    # print(query)
    result = ut_ds.running_searchqury(query)
    for i in result:
      # print(i[0])
      tc_dict[i[0]] = us_dict[key]
  print(f"Printing the test cases based on the importance value calculated for the user stories:{len(tc_dict)}{tc_dict}")
  tc_list = list(tc_dict.keys())
  return (tc_dict, tc_list)
  # query = ut.create_searchquery(us_list, "tc_id", ustcmap_tablename, "us_id", ds_id, "")
  # result = ut_ds.running_searchqury(query)
  # tc_list = []
  # for ind,i in enumerate(result):
  #   tc_list.append(result[ind][0])
  # print(f"Printing the selected set of test cases based on the user story selection: {sorted(tc_list)}")
  # print(f"Number of test cases selected = {len(tc_list)} out of a total of {total_tccount} test cases")
  # print(f"Selection rate: {(len(tc_list) / total_tccount) * 100}")
  # return sorted(tc_list)


def creation_defectsubset(tc_list, ds_id):
  query = ut.create_searchquery(tc_list, "defect_id", tcdefectmap_tablename, "tc_id", ds_id,  "")
  result = ut_ds.running_searchqury(query)
  defect_list = []
  for ind,i in enumerate(result):
    defect_list.append(result[ind][0])
  print(f"Printing the identified set of defects based on the selected subset of test cases: {sorted(defect_list)}")
  print(f"Number of defects identified = {len(defect_list)} out of a total of {total_defectcount} defects")
  return sorted(defect_list)


def measuring_valuepreserved(us_list, tc_list, ds_id):
  totalvalue_preserved = 0
  for i in us_list:
    query1 = f"Select tc_id from us_tc_map where us_id = {i} and ds_id = '{ds_id}'"
    query2 = f"Select us_businessvalue from userstory_datasettable where us_id = {i} and ds_id = '{ds_id}'"
    query3 = f"Select sum(us_businessvalue) from userstory_datasettable where us_id in ({str(us_list).replace('[', '').replace(']', '')}) and ds_id = '{ds_id}'"
    result1 = ut_ds.running_searchqury(query1)
    result3 = ut_ds.running_searchqury(query3)
    temptc_list = ut.createlist_fromdbresult(result1,0)
    if temptc_list is not None:
      all_present = all(element in tc_list for element in temptc_list)
      if all_present:
        # print("all same")
        result2 = ut_ds.running_searchqury(query2)
        totalvalue_preserved += result2[0][0]
      # else:
      #   print(f"All not present for us_id: {i} where temptc_list is: {temptc_list}")
  print(f"totalvalue_preserved: {totalvalue_preserved} out of {result3[0][0]}")
  return totalvalue_preserved, result3[0][0]

def runningalgo_fixedtime_randomselection(totalexectime, tcexectime_fixed, us_list, ds_id):
  print("inside random algo")
  query = f"Select tc_id from us_tc_map where us_id in ({str(us_list).replace('[', '').replace(']', '')}) and ds_id = '{ds_id}'"
  result = ut_ds.running_searchqury(query)
  total_tclist = ut.createlist_fromdbresult(result,0)
  # print(len(total_tclist), total_tclist)
  total_allowedtc = int(totalexectime/tcexectime_fixed)
  if total_allowedtc<len(total_tclist):
    selectedtc_list = random.sample(total_tclist,total_allowedtc)
  else:
    selectedtc_list = total_tclist
  # print(f"selectedtc_list: {len(selectedtc_list), selectedtc_list}")
  print("Running Random selection process for RTS:")
  print(f"Total test cases selected with fixed execution time of test cases= {len(selectedtc_list)} out of {len(total_tclist)}")
  print(f"Selected test cases through random selection: {selectedtc_list}")
  return selectedtc_list


def saving_results(runconfig, ds_id):
  if runconfig == "2":
    col_name = "results"
  elif runconfig == "1.1":
    col_name = "results_config1"
  elif runconfig == "1.2":
    col_name = "results_config1_2"
  elif runconfig == "1.3":
    col_name = "results_config1_3"
  elif runconfig == "0":
    col_name = "results_config0"
  result_text = ut.read_from_txt(outputfilename)
  print(f"filename: {outputfilename}")
  query_updateresults = ut.updatetable_query(dataset_tablename, col_name, result_text, "str", ds_id)
  ut_ds.running_insertquery(query_updateresults)

# def saving_results_forconfig1():
#   result_text = ut.read_from_txt(outputfilename)
#   print(f"filename: {outputfilename}")
#   query_updateresults = ut.updatetable_query(dataset_tablename, "results_config1", result_text, "str", ds_id_res)
#   ut_ds.running_insertquery(query_updateresults)
#
# def saving_results_forconfig1_2():
#   result_text = ut.read_from_txt(outputfilename)
#   print(f"filename: {outputfilename}")
#   query_updateresults = ut.updatetable_query(dataset_tablename, "results_config1_2", result_text, "str", ds_id_res)
#   ut_ds.running_insertquery(query_updateresults)
#
# def saving_results_forconfig1_3():
#   result_text = ut.read_from_txt(outputfilename)
#   print(f"filename: {outputfilename}")
#   query_updateresults = ut.updatetable_query(dataset_tablename, "results_config1_3", result_text, "str", ds_id_res)
#   ut_ds.running_insertquery(query_updateresults)
#
# def saving_results_forconfig0():
#   result_text = ut.read_from_txt(outputfilename)
#   print(f"filename: {outputfilename}")
#   query_updateresults = ut.updatetable_query(dataset_tablename, "results_config0", result_text, "str", ds_id_res)
#   ut_ds.running_insertquery(query_updateresults)


def saving_config(ds_id):
  json_data = ut_ds.ini_to_json(configfilename)
  ut_ds.insert_json_data(json_data, ds_id)

for indi, i in enumerate(dsid_list):
  ds_id_res = ds_id = str(i)
  total_executiontime = total_executiontime_list[indi]
  for j in importanceval_calconfig:
    try:
      print(f"ds_id: {ds_id}, computation configuration: {j}, total execution window: {total_executiontime}")
      us_dict = get_usdict(ds_id, j)
      us_list = list(us_dict.keys())
      tc_dict, tc_list = ut.copy_console('a', creation_tcsubset, us_dict, ds_id)
      # sorted_tcdict = ut.copy_console('a',ut_ds.creating_prioritydict_tclist,tc_list, ds_id)
      tcset_fixedexectime = ut.copy_console('a', createsubset.creatingtcset_fixedexecutiontime, tc_dict, total_executiontime, tcexectime_fixed)
      ut_ds.readandwrite_toexcel(ds_id, "J", tcexectime_fixed)
      ut_ds.readandwrite_toexcel(ds_id, "K", total_executiontime)
      ut_ds.readandwrite_toexcel(ds_id, "L", len(tcset_fixedexectime))
      value_preserved, totalvalue = ut.copy_console('a', measuring_valuepreserved, us_list, tcset_fixedexectime, ds_id)
      ut_ds.readandwrite_toexcel(ds_id, "M", totalvalue)
      if j == "1.1":
        valuepreserved_col = "N"
      elif j == "1.2":
        valuepreserved_col = "O"
      elif j == "1.3":
        valuepreserved_col = "P"
      elif j == "0":
        valuepreserved_col = "Q"
      ut_ds.readandwrite_toexcel(ds_id, valuepreserved_col, value_preserved)
      tcset_fixedexectime_randomselection = ut.copy_console('a', runningalgo_fixedtime_randomselection, total_executiontime, tcexectime_fixed, us_list, ds_id)
      print(tcset_fixedexectime_randomselection)
      value_preserved_random, total_value = ut.copy_console('a', measuring_valuepreserved, us_list, tcset_fixedexectime_randomselection, ds_id)
      ut_ds.readandwrite_toexcel(ds_id, "R", value_preserved_random)
      saving_results(j, ds_id)
    except:
      print(f"Problem faced while running ds_id: {i} so skipped")



# tcexec_dict = ut.copy_console('a', createsubset.create_tcdict_exectime, tc_list, ds_id)  # Creating a dictionary where TC# is the key and its execution time is the value
# print(f"sorted_tcdict {tc_dict}")
# print(f"tc_list:{tc_list}")
# print(f"tcexec_dict {tcexec_dict}")
# ut.copy_console('a', createsubset.creatingtcset_varyingecutiontime, tc_dict, total_executiontime, tcexec_dict)    # Creating a smaller subset of test cases based on the variable exacution time for each test case
# defect_list = ut.copy_console('a', creation_defectsubset, tc_list)


# saving_results(importanceval_calconfig)

# ut.saving_config(configfilename, next_id)


