import random

import mysql.connector
import configparser
import utilities_dataset as ut_ds
import utilities as ut
from datetime import datetime
# import fill_primarytables as currid

curr_id = ut_ds.getds_id()
next_id = int(curr_id) + 1

def initimple(next_id):
  print(f"new next id: {next_id}")
  outputfile_name = "output.txt"
  inifilename_stored = "inifile_name.txt"
  config = configparser.ConfigParser()
  config.read('config1.ini')
  run_config = config['run_configuration']
  tablenames_config = config['tablenames']
  dataset_tablename = tablenames_config["dataset_tablename"]
  # usselection_config = "random"   #random or serialized
  # next_id = 1

  config_type = run_config['run_config']
  curr_id = ut_ds.getds_id()
  current_datetime = datetime.now()
  formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  if config_type == "new":
    if curr_id is None:
      next_id = 1
    # else:
    #   # next_id = int(curr_id)+1
    cols = ["ds_id", "run_config", "timestamp"]
    vals = [next_id, config_type, formatted_datetime]
    datatype = ["str", "str", "str"]
    query = ut.insertquery_creation(dataset_tablename, cols, vals, datatype)
    ut_ds.running_insertquery(query)
    ut.write_to_txt(inifilename_stored, "config1.ini")
    print("Finished insert query")

  elif config_type == "copy":
    # print("I am inside")
    # next_id = int(curr_id) + 1
    config_copiedfrom = run_config["config_copiedfrom"]
    print(f"config_copiedfrom: {config_copiedfrom}")
    cols = ["ds_id", "run_config", "config_copiedfrom", "timestamp"]
    vals = [next_id, config_type, config_copiedfrom, formatted_datetime]
    datatype = ["str", "str", "str", "str"]
    query = ut.insertquery_creation(dataset_tablename, cols, vals, datatype)
    ut_ds.running_insertquery(query)
    query_inifile = f"Select ini_file from dataset where ds_id = '{config_copiedfrom}'"
    inifile_res = ut_ds.running_searchqury(query_inifile)
    inicontent = inifile_res[0][0]
    ut_ds.json_to_ini(inicontent)
    ut.write_to_txt(inifilename_stored, 'copiedconfig.ini')


    # copy_ds_id = run_config["copy_ds_id"]
    # if copy_ds_id.lower() != "yes":
    #   ut.write_to_txt(inifilename_stored,'copiedconfig.ini')
    # elif copy_ds_id.lower() == "yes":
    #   ut.write_to_txt(inifilename_stored,f'copiedconfig.ini\n{config_copiedfrom}')

  else:
    print(f"Wrong input for config_type == {config_type}")

# initimple()