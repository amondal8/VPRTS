import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Aa*231491*dD",
  database="new1"
)


def tabledrop(table_name):
  return f"""DROP TABLE {table_name}"""


def droptables(query1, query2, query3):
  mydb.start_transaction()
  mycursor = mydb.cursor()
  mycursor.execute(query1)
  mycursor.execute(query2)
  mycursor.execute(query3)
  # print('I am inside')
  mydb.commit()
  mycursor.close()
  mydb.close()
