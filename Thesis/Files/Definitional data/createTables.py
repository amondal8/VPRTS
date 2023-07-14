import mysql.connector
import configparser
# import fill_primarytables as currid

config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect = config['dbconnection']
configuration = config['configuration']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

tablecreation_config = configuration['tablecreate_config']


# def tablecreation_idtracker(table_name):
#   return f"""CREATE TABLE {table_name}(
#               id INT Primary key,
#               comments VARCHAR(500),
#               timestamp DATETIME)"""


def tablecreation_userstory(table_name):
  return f"""CREATE TABLE {table_name}(
              us_id VARCHAR(10) Primary key,
              us_desc VARCHAR(500));"""
#need to provide a release


def tablecreation_userstoryvalue(table_name):
  return f"""CREATE TABLE {table_name}(
              us_points INT,
              us_businessvalue INT DEFAULT 0);"""


def tablecreation_releasedata(table_name):
  return f"""CREATE TABLE {table_name}(
                release_id INT PRIMARY KEY,
                start_date DATE DEFAULT NULL,
                end_date DATE DEFAULT NULL);"""


def tablecreation_sprintdata(table_name):
  return f"""CREATE TABLE {table_name}(
                sprint_id INT PRIMARY KEY,
                start_date DATE DEFAULT NULL,
                end_date DATE DEFAULT NULL);"""



def tablecreation_testcase(table_name):
  return f"""CREATE TABLE {table_name}(
                tc_id VARCHAR(10) Primary Key,
                tc_name VARCHAR(100) DEFAULT NULL,
                tc_desc VARCHAR(500) DEFAULT NULL,
                tc_prerequisite VARCHAR(500) DEFAULT NULL,
                tc_setup VARCHAR(500) DEFAULT NULL,
                tc_steps VARCHAR(500) DEFAULT NULL,
                tc_expectedresults VARCHAR(500) DEFAULT NULL,
                tc_sampletestdata VARCHAR(200) DEFAULT NULL);"""


def tablecreation_tcexectime(table_name):
  return f"""CREATE TABLE {table_name}(
                tc_executiontime INT DEFAULT 0,
                tc_setup INT DEFAUlT 0,
                tc_teardown INT DEFAULT 0,
                tc_additionalres INT DEFAULT 0);"""


def tablecreation_defect(table_name):
  return f"""CREATE TABLE {table_name}(
                  defect_id VARCHAR(10),
                  defect_desc VARCHAR(500) DEFAULT NULL,
                  affected_version VARCHAR(50) DEFAULT NULL,
                  steps_to_reproduce VARCHAR(1000) DEFAULT NULL,
                  expected_result VARCHAR(500) DEFAULT NULL,
                  environment VARCHAR(100) DEFAULT NULL);"""


def tablecreation_defectseverity(table_name):
  return f"""CREATE TABLE {table_name}(
                  defect_severity_id INT Primary key,
                  defect_severity_desc VARCHAR(20));"""


def tablecreation_defectpriority(table_name):
  return f"""CREATE TABLE {table_name}(
                  defect_priority_id INT Primary key,
                  defect_priority_desc VARCHAR(20));"""


def tablecreation_defectcomplexity(table_name):
  return f"""CREATE TABLE {table_name}(
                  defect_complexity_id INT Primary Key,
                  defect_complexity_desc VARCHAR(20));"""


def tablecreation_tcstatus(table_name):
  return f"""CREATE TABLE {table_name}(
                    status_id INT PRIMARY KEY,
                    status_desc VARCHAR(20));"""


def tablecreation_tcrunhistory(table_name):
  return f"""CREATE TABLE {table_name}(
                    execution_date DATE);"""


def tablecreation_codemodule(table_name):
  return f"""CREATE TABLE {table_name}(
                    cm_id INT PRIMARY KEY,
                    cm_desc VARCHAR(500) DEFAULT NULL);"""


def tablecreation_tcmap(table_name):
  return f"""CREATE TABLE {table_name}(
                    us_id VARCHAR(10),
                    tc_id VARCHAR(10),
                    track_id INT,
                    PRIMARY KEY(us_id, tc_id, track_id));"""


def tablecreation_defectmap(table_name):
  return f"""CREATE TABLE {table_name}(
                    tc_id VARCHAR(10),
                    defect_id VARCHAR(10),
                    track_id INT,
                    PRIMARY KEY(tc_id, defect_id, track_id));"""


#additional resource required to run test cases
def tablecreation_additionalresourcelist(table_name):
  return f"""CREATE TABLE {table_name}(
                    resource_id INT Primary Key,
                    resource_desc VARCHAR(100));"""

# # query1 = tablecreation_idtracker("idtracker")
# query2 = tablecreation_userstory("user_story")
# query3 = tablecreation_testcase("testcase")
# query4 = tablecreation_defect("defect")
# query5 = tablecreation_tcmap("us_tc_map")
# query6 = tablecreation_defectmap("tc_defect_map")

query1 = tablecreation_userstory("userstory")
query2 = tablecreation_userstoryvalue("userstoryvalue")
query3 = tablecreation_testcase("testcase")
query4 = tablecreation_tcexectime("tcexectime")
query5 = tablecreation_defect("defect")
query6 = tablecreation_defectseverity("defect_severity")
query7 = tablecreation_defectpriority("defect_priority")
query8 = tablecreation_defectcomplexity("defect_complexity")
query9 = tablecreation_releasedata("release_data")
query10 = tablecreation_sprintdata("sprint_data")
query11 = tablecreation_tcstatus("tc_runstatus")
query12 = tablecreation_tcrunhistory("tc_executionhistory")
query13 = tablecreation_codemodule("code_module")
query14 = tablecreation_additionalresourcelist("addresource_tcexecution")

# query9 = tablecreation_tcmap("us_tc_map")
# query10 = tablecreation_defectmap("tc_defect_map")

querylist = [query1, query2, query3, query4, query5, query6, query7, query8, query9, query10, query11, query12, query13, query14]

def createtables(querylist):
  mydb.start_transaction()
  mycursor = mydb.cursor()
  for ind, i in enumerate(querylist):
    mycursor.execute(i)
    print(f"Created table# {ind+1}")
  mydb.commit()
  mycursor.close()
  mydb.close()

createtables(querylist)


