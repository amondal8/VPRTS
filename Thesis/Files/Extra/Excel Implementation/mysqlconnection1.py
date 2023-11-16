import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="Aa*231491*dD",
  database="new1"
)
pid_list=[1,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,42,43,44]

def dbcreation_query(db_name):
    return f"CREATE DATABASE {db_name}"

def tablecreation_query(table_name):
    return f"""CREATE TABLE {table_name}(
                us_id INT Primary key,
                us_desc VARCHAR(500),
                us_points INT)"""



def query(issue_type, project_id):
    return f"""select a.* from issue a, project b, affected_version c, version d
    where  a.Type='{issue_type}'
    and b.ID = d.Project_ID
    and d.ID=c.Affected_Version_ID
    and c.Issue_ID=a.ID
    and a.Project_ID={project_id}
    and Description_Text is NOT NULL
    order by a.id"""
def runner():
# for i in pid_list:

    # query1=query("Story", i)
    # query2=query("Bug", i)
    #
    mydb.start_transaction()
    mycursor = mydb.cursor()
    # mycursor.execute(dbcreation_query("new1"))
    # mycursor.execute(tablecreation_query("user_stories"))

    mycursor.execute("Insert into user_stories (us_id, us_desc, us_points) values (2, 'us2_desc', 20)")
    # mycursor.execute("select * from user_stories")
    # result1 = mycursor.fetchall()
    # print(result1)

    mydb.commit()
    mycursor.close()
    mydb.close()

# for row in result:
#   print(row)

runner()
