import mysql.connector
import openpyxl as op
import configparser
import json

file = "ini1"
config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect = config['dbconnection_dataset']
data = config['data']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)



filepath = "C:/Users/amondal8/PycharmProjects/pythonProject3/Thesis/Files/Database Creation/Mapping.xlsx"
workbook = op.load_workbook(filepath)

def getds_id():
  print(dbconnect["database"])
  mycursor = mydb.cursor()
  mycursor.execute("Select ds_id from dataset ORDER BY timestamp DESC LIMIT 1")
  result = mycursor.fetchone()
  if result is None:
    return result
  else:
    return result[0]


def stringcreation_columns(my_list):
  my_str = ""
  for ind, i in enumerate(my_list):
    if ind == 0 and len(my_list) != 1:
      my_str = my_str + "(" + str(i)
    elif ind ==0 and len(my_list) == 1:
      my_str = my_str + "(" + str(i) + ")"
    elif ind == len(my_list) - 1:
      my_str = my_str + "," + str(i) + ")"
    else:
      my_str = my_str + "," + str(i)
  return my_str


def stringcreation_values(my_list, datatype_list):
  my_str = ""
  for ind, i in enumerate(my_list):
    if ind == 0 and len(my_list) != 1:
      if datatype_list[ind] == "int":
        my_str = my_str + "(" + str(i)
      else:
        my_str = my_str + "(\"" + str(i) + "\""
    elif ind == 0 and len(my_list) == 1:
      if datatype_list[ind] == "int":
        my_str = my_str + "(" + str(i) + ")"
      else:
        my_str = my_str + "(\"" + str(i) + "\")"
    elif ind == len(my_list) - 1:
      if datatype_list[ind] == "int":
        my_str = my_str + "," + str(i) + ")"
      else:
        my_str = my_str + ",\"" + str(i) + "\")"
    else:
      if datatype_list[ind] == "int":
        my_str = my_str + "," + str(i)
      else:
        my_str = my_str + ",\"" + str(i) + "\""
  return my_str


def running_insertquery(query):
  mydb = mysql.connector.connect(
    host=dbconnect["host"],
    user=dbconnect["user"],
    password=dbconnect["password"],
    database=dbconnect["database"]
  )
  mycursor = mydb.cursor()
  if mydb.is_closed():
    mydb.start_transaction()
  # mycursor = cc.connection()
  mycursor.execute(query)
  # print(f"Query {query} executed successfully")
  mydb.commit()
  # cc.closeconnection()
  mycursor.close()
  mydb.close()


def createdictfromexcel(filepath, worksheetName, keycol, valuecol):
  workbook = op.load_workbook(filepath)
  worksheet = workbook[worksheetName]
  maxr = worksheet.max_row
  keyval_dict = {}

  for row_ind, row in enumerate(worksheet.iter_rows(min_row=1, max_row=maxr, min_col=keycol, max_col=keycol),
                                start=1):
    for cell in row:
      valcell = worksheet.cell(row=row_ind, column=valuecol)
      val = valcell.value
      # if value is None:
      #     value=None
      keyval_dict[cell.value] = val
  # print(keyval_dict)
  return keyval_dict


def fetch_ones_in_row(adjacency_matrix, row_index):
  row = adjacency_matrix[row_index]
  ones_indices = [index for index, value in enumerate(row) if value == 1]
  return ones_indices


def running_searchqury(query):
  mycursor = mydb.cursor()
  mycursor.execute(query)
  result = mycursor.fetchall()
  # print(result)
  return result

def create_fetchquery_usvalue(colname, tc_id, ds_id):
  query = f"""Select sum({colname}) from userstory_datasettable where us_id in(SELECT DISTINCT us_id from us_tc_map where tc_id in ("{tc_id}") and ds_id = {ds_id}) and ds_id = {ds_id}"""
  # print(query)
  return query


def create_fetchquery_tcexectime(colname, tc_id, ds_id):
  query = f"""SELECT {colname} from tc_datasettable where tc_id = "{tc_id}" and ds_id = "{ds_id}"; """
  print(query)
  return query


def creating_prioritydict_tclist(tc_list, ds_id):
  tc_dict = {}
  for ind, i in enumerate(tc_list):
    query_usp = create_fetchquery_usvalue("us_points", i, ds_id)
    query_usbv = create_fetchquery_usvalue("us_businessvalue", i, ds_id)
    # print(query)
    result1 = running_searchqury(query_usp)
    result2 = running_searchqury(query_usbv)
    tc_dict[i] = int(result1[0][0]) + int(result2[0][0])
  sorted_tcdict = dict(sorted(tc_dict.items(), key=lambda x: x[1], reverse=True))
  print(f"Printing the selected tc set with usp: {tc_dict}")
  print(f"Printing the selected set in decreasing order of usp: {sorted_tcdict}")
  return sorted_tcdict


def ini_to_json(ini_filepath):
  # Read the .ini file
  config = configparser.ConfigParser()
  config.read(ini_filepath)

  # Convert the .ini file to a dictionary
  ini_dict = {}
  for section in config.sections():
    ini_dict[section] = dict(config[section])

  # Convert the dictionary to a JSON string
  json_string = json.dumps(ini_dict, indent=1)

  return json_string


def insert_json_data(json_data, ds_id):
  sql_insert_query = f"UPDATE dataset SET ini_file = ('{json_data}') where ds_id = '{ds_id}'"
  # print(sql_insert_query)
  running_insertquery(sql_insert_query)


def json_to_ini(json_data):
  data_dict = json.loads(json_data)
  # Add each key-value pair to the 'DEFAULT' section of the .ini file
  for key, value in data_dict.items():
    config[key] = value

  with open('copiedconfig.ini', 'w') as configfile:
    config.write(configfile)




# json_data = ini_to_json("config1.ini")
# print(json_data)
# # insert_json_data(json_data, 1)
# json_to_ini(json_data)
# json_data = ini_to_json("copiedconfig.ini")
# print(json_data)

# creating_prioritydict_tclist(["TC1", "TC2"], "1")

# us_lst = [1,2,3,4]
# create_tcsearchquery(us_lst, "tc_id", "us_tc_map", "us_id")