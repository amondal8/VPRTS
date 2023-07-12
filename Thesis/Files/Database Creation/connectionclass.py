import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Aa*231491*dD",
  database="new1"
)

class connection:
  def __init__(self):
    mydb.start_transaction()
    mycursor = mydb.cursor()
    return mycursor

  def closeconnection(self):
    mydb.close


def runningquery(query):
  if mydb.is_closed():
    mydb.start_transaction()
  mycursor = mydb.cursor()
  mycursor.execute(query)
  print(f"Query {query} executed successfully")
  mydb.commit()
  mycursor.close()
  mydb.close()





# gettrack_id()


# column=["id", "comments", "timestamp"]
# values = [1, "test data", "121921"]
# datatype = ["int", "str", "str"]
# print(insertquery_creation("idtracker", column, values, datatype))
