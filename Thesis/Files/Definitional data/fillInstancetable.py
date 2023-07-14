import random

import mysql.connector
import configparser
import utilities as ut
# import fill_primarytables as currid

config = configparser.ConfigParser()
config.read('config1.ini')
dbconnect = config['dbconnection']
configuration = config['configuration']
data = config['data']

mydb = mysql.connector.connect(
  host=dbconnect["host"],
  user=dbconnect["user"],
  password=dbconnect["password"],
  database=dbconnect["database"]
)

rel1 = data['release1'].split(',')
rel2 = data['release2'].split(',')
uscount_r1 = 10
uscount_r2 = 10
usselection_config = "random"   #random or serialized
# tablecreation_config = configuration['tablecreate_config']

def fillinsttable_usstory():
  usr1count_flag = 0
  usr2count_flag = 0
  tablename_usinstance = "userstory_insttable"
  cols = ['us_id', 'us_desc', 'release_id', 'us_points', 'us_businessvalue']
  dtype = ['int', 'str', 'int','int','int']
  query_usid = "select us_id, us_desc from userstory;"
  query_releaseid = "select release_id from release_data"
  query_usp = "select us_points,us_businessvalue from userstoryvalue"
  usid_res = ut.running_searchqury(query_usid)
  relid_res = ut.running_searchqury(query_releaseid)
  usv_res = ut.running_searchqury(query_usp)
  usdesclist_rel1 = []
  usdesclist_rel12 = []

  usid_list = ut.createlist_fromdbresult(usid_res,0)
  usdesc_list = ut.createlist_fromdbresult(usid_res,1)
  relid_list = ut.createlist_fromdbresult(relid_res,0)
  usp_list = ut.createlist_fromdbresult(usv_res,0)
  usbv_list = ut.createlist_fromdbresult(usv_res, 1)

  uslist_rel1 = random.sample(usid_res,uscount_r1)

  for i in uslist_rel1:
    if i in usid_res:
      usid_res.remove(i)

  uslist_rel2 = random.sample(usid_res,uscount_r2)
  usidlist_rel1 = ut.createlist_fromdbresult(uslist_rel1,0)
  usdesclist_rel1 = ut.createlist_fromdbresult(uslist_rel1,1)
  usidlist_rel2 = ut.createlist_fromdbresult(uslist_rel2, 0)
  usdesclist_rel2 = ut.createlist_fromdbresult(uslist_rel2, 1)

  usvlist_rel1 = random.sample(usv_res, uscount_r1)

  for i in usvlist_rel1:
    if i in usv_res:
      usv_res.remove(i)

  usvlist_rel2 = random.sample(usv_res, uscount_r2)
  usplist_rel1 = ut.createlist_fromdbresult(usvlist_rel1, 0)
  usbvlist_rel1 = ut.createlist_fromdbresult(usvlist_rel1, 1)
  usplist_rel2 = ut.createlist_fromdbresult(usvlist_rel2, 0)
  usbvlist_rel2 = ut.createlist_fromdbresult(usvlist_rel2, 1)

  insertingvalue_usinsttable(usidlist_rel1, usdesclist_rel1, rel1, usplist_rel1, usbvlist_rel1, tablename_usinstance, cols, dtype)
  insertingvalue_usinsttable(usidlist_rel2, usdesclist_rel2, rel2, usplist_rel2, usbvlist_rel2, tablename_usinstance, cols, dtype)


def insertingvalue_usinsttable(usidlist, usdesclist, relid, usplist, usbvlist, tablename, cols, dtype):

  for ind, i in enumerate(usidlist):
    usid_val = i
    usdesc_val = usdesclist[ind]
    relid_val = int(random.choice(relid))
    usp_val = usplist[ind]
    usbv_val = usbvlist[ind]

    vals = [usid_val, usdesc_val, relid_val, usp_val, usbv_val]
    query = ut.insertquery_creation(tablename, cols, vals, dtype)
    print(f"query is : {query}")
    ut.running_insertquery(query)


# def fillinsttable_testcase():



fillinsttable_usstory()