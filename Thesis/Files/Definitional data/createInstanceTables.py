import mysql.connector
import configparser
import sqlite3
# import fill_primarytables as currid

config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect_def = config['dbconnection']
dbconnect = config['dbconnection_dataset']
tablenames_config = config['tablenames']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

definitional_database = dbconnect_def["database"]
#Primary tablenames
us_tablename = tablenames_config["us_tablename"]
tc_tablename = tablenames_config["tc_tablename"]
defect_tablename = tablenames_config["defect_tablename"]
codemodule_tablename = tablenames_config["codemodule_tablename"]

#Dataset tablenames
dataset_tablename = tablenames_config["dataset_tablename"]
usdatasettable_tablename = tablenames_config["usdatasettable_tablename"]
tcdatasettable_tablename = tablenames_config["tcdatasettable_tablename"]
defectdatasettable_tablename = tablenames_config["defectdatasettable_tablename"]
cmdatasettable_tablename = tablenames_config["cmdatasettable_tablename"]
ustcmap_tablename = tablenames_config["ustcmap_tablename"]
tcdefectmap_tablename = tablenames_config["tcdefectmap_tablename"]
uscmmap_tablename = tablenames_config["uscmmap_tablename"]




def datasettablecreation_dataset(table_name):   #run_config values will be "new" or "old". "runconfig_id" is the ds_id if the run_config value is set to "old"
  return f"""CREATE TABLE {table_name}(
              ds_id VARCHAR(10) Primary key,
              run_config VARCHAR(20),
              config_copiedfrom  VARCHAR(10) DEFAULT NULL,
              timestamp DATETIME, 
              algorithm VARCHAR(200),
              parameters VARCHAR(1000),
              environment VARCHAR(100),
              results VARCHAR(5000),
              ini_file JSON);"""


def datasettablecreation_userstory(table_name):
  return f"""CREATE TABLE {table_name}(
              ds_id VARCHAR(10),
              us_id VARCHAR(10),
              us_desc VARCHAR(500),
              release_id INT,
              us_points INT,
              us_businessvalue INT,
              FOREIGN KEY (us_id) REFERENCES {definitional_database}.{us_tablename} (us_id));"""


def datasettablecreation_testcase(table_name):
  return f"""CREATE TABLE {table_name}(
              ds_id VARCHAR(10),
              tc_id VARCHAR(10),
              tc_executiontime INT,
              tc_setuptime INT,
              tc_teardowntime INT,
              tc_additionalres INT,
              FOREIGN KEY (tc_id) REFERENCES {definitional_database}.{tc_tablename} (tc_id));"""


def datasettablecreation_defect(table_name):
  return f"""CREATE TABLE {table_name}(
              ds_id VARCHAR(10),
              defect_id VARCHAR(10),
              defect_severity_id INT,
              defect_priority_id INT,
              defect_complexity_id INT,
              FOREIGN KEY (defect_id) REFERENCES {definitional_database}.{defect_tablename} (defect_id));"""


def datasettablecreation_cm(table_name):
  return f"""CREATE TABLE {table_name}(
              ds_id VARCHAR(10),
              cm_id VARCHAR(10),
              release_id INT,
              FOREIGN KEY (cm_id) REFERENCES {definitional_database}.{codemodule_tablename} (cm_id));"""


def datasettablecreation_tcmap(table_name):
  return f"""CREATE TABLE {table_name}(
                    us_id VARCHAR(10),
                    tc_id VARCHAR(10),
                    ds_id VARCHAR(10),
                    PRIMARY KEY(us_id, tc_id, ds_id));"""


def datasettablecreation_cmmap(table_name):
  return f"""CREATE TABLE {table_name}(
                    us_id VARCHAR(10),
                    cm_id VARCHAR(10),
                    affected_value VARCHAR(50),
                    ds_id VARCHAR(10),
                    PRIMARY KEY(us_id, cm_id, ds_id));"""


def datasettablecreation_defectmap(table_name):
  return f"""CREATE TABLE {table_name}(
                    tc_id VARCHAR(10),
                    defect_id VARCHAR(10),
                    ds_id VARCHAR(10),
                    PRIMARY KEY(tc_id, defect_id, ds_id));"""


query1 = datasettablecreation_dataset(dataset_tablename)
query2 = datasettablecreation_userstory(usdatasettable_tablename)
query3 = datasettablecreation_testcase(tcdatasettable_tablename)
query4 = datasettablecreation_defect(defectdatasettable_tablename)
query5 = datasettablecreation_cm(cmdatasettable_tablename)
query6 = datasettablecreation_tcmap(ustcmap_tablename)
query7 = datasettablecreation_cmmap(uscmmap_tablename)
query8 = datasettablecreation_defectmap(tcdefectmap_tablename)


querylist = [query1, query2, query3, query4, query5, query6, query7, query8]

def createtables(querylist):
  mydb.start_transaction()
  mycursor = mydb.cursor()
  for ind, i in enumerate(querylist):
    try:
      mycursor.execute(i)
      print(f"Created table# {ind+1}")
    except Exception as e:
      print(f"Query {ind+1} Error while table creation with error message: {str(e)}. Moving to next table")
      continue
  mydb.commit()
  mycursor.close()
  mydb.close()

createtables(querylist)


