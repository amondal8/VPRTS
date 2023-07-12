import mysql.connector
import configparser
# import fill_primarytables as currid

config = configparser.ConfigParser()
config.read('config.ini')
dbconnect = config['dbconnection']
configuration = config['configuration']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

tablecreation_config = configuration['tablecreate_config']



def tablecreation_idtracker(table_name):
  return f"""CREATE TABLE {table_name}(
              id INT Primary key,
              comments VARCHAR(500),
              timestamp DATETIME)"""

def tablecreation_userstory(table_name):
  return f"""CREATE TABLE {table_name}(
              us_id VARCHAR(10),
              us_desc VARCHAR(500),
              us_points INT,
              release_id INT,
              track_id INT,
              PRIMARY KEY(us_id, track_id));"""
#need to provide a release

def tablecreation_testcase(table_name):
  return f"""CREATE TABLE {table_name}(
                tc_id VARCHAR(10),
                tc_desc VARCHAR(500),
                tc_executiontime INT,
                track_id INT,
                PRIMARY KEY(tc_id, track_id));"""

def tablecreation_defect(table_name):
  return f"""CREATE TABLE {table_name}(
                  defect_id VARCHAR(10),
                  defect_desc VARCHAR(500),
                  track_id INT,
                  PRIMARY KEY(defect_id, track_id));"""

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

query1 = tablecreation_idtracker("idtracker")
query2 = tablecreation_userstory("user_story")
query3 = tablecreation_testcase("testcase")
query4 = tablecreation_defect("defect")
query5 = tablecreation_tcmap("us_tc_map")
query6 = tablecreation_defectmap("tc_defect_map")

querylist = [query1, query2, query3, query4, query5, query6]

def createtables(querylist):
  mydb.start_transaction()
  mycursor = mydb.cursor()
  for ind, i in enumerate(querylist):
    mycursor.execute(i)
    print(f"Created table# {ind}")
  mydb.commit()
  mycursor.close()
  mydb.close()

createtables(querylist)


