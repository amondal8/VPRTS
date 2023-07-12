import mysql.connector
import configparser
import openpyxl as op
import utilities as ut
from datetime import datetime
import pandas as pd
import matrixcreation as matc
import defectmapping as defmap


filepath = "C:/Users/amondal8/PycharmProjects/pythonProject3/Thesis/Files/Database Creation/Mapping.xlsx"
df = pd.read_excel(filepath)
workbook = op.load_workbook(filepath)
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
# tc_count = matc.total_tccount
connection_prob_tcmap = 1   # Using a value less than 1 will decrease the 1s even more, so use it wisely
connection_prob_defectmap = .5
limiting_ones = 8
adj_matrixtcmap = []
adj_matrixdefectmap = []
total_uscount = int(dataconfig["us_totalcount"])
total_tccount = int(dataconfig["tc_totalcount"])
total_defectcount = int(dataconfig["defect_totalcount"])
tc_prefix = dataconfig["tc_prefix"]
defect_prefix = dataconfig["defect_prefix"]
lower_limitones = 0
upper_limitones = 4


config_type = configure['tablecreate_config']
next_id = ut.gettrack_id()

adj_matrixtcmap = matc.generate_random_adjmat_withlimits(total_uscount, total_tccount, connection_prob_tcmap, limiting_ones)
matc.writematto_reqmappingexcel(adj_matrixtcmap)
matc.writeto_revReqMat_excel(adj_matrixtcmap)
adj_matrixdefectmap = defmap.generate_defectmap_adjmat_withlimits(total_tccount, total_defectcount, connection_prob_defectmap, lower_limitones, upper_limitones)
defmap.writematto_defectmappingexcel(adj_matrixdefectmap)


def filltable_ustcmap():
  print(adj_matrixtcmap)
  cols = ['us_id', 'tc_id', 'track_id']
  dtype = ['str', 'str', 'int']
  for row in range(len(adj_matrixtcmap)):
    ones_list = ut.fetch_ones_in_row(adj_matrixtcmap, row)
    for i in ones_list:
      vals = ["R1_"+str(row+1), tc_prefix+str(i+1), next_id]
      query = ut.insertquery_creation(ustcmap_tablename, cols, vals, dtype)
      print(f"query is : {query}")
      ut.running_insertquery(query)



def filltable_tcdefectsmap():
  print(adj_matrixdefectmap)
  cols = ['tc_id', 'defect_id', 'track_id']
  dtype = ['str', 'str', 'int']
  for row in range(len(adj_matrixdefectmap)):
    ones_list = ut.fetch_ones_in_row(adj_matrixdefectmap, row)
    for i in ones_list:
      vals = [tc_prefix + str(row + 1), defect_prefix + str(i + 1), next_id]
      query = ut.insertquery_creation(tcdefectmap_tablename, cols, vals, dtype)
      print(f"query is : {query}")
      ut.running_insertquery(query)


filltable_ustcmap()
filltable_tcdefectsmap()
