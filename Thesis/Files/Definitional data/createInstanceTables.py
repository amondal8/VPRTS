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



def insttablecreation_userstory(table_name):
  return f"""CREATE TABLE {table_name}(
              us_id VARCHAR(10) Primary key,
              us_desc VARCHAR(500),
              release_id INT,
              us_points INT,
              us_businessvalue INT);"""
#need to provide a release


query1 = insttablecreation_userstory("userstory_insttable")



querylist = [query1]

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


