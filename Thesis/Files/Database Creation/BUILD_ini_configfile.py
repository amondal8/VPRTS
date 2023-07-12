import configparser

config = configparser.ConfigParser()

config.add_section('tablecreation')
config.set('tablecreation', 'creation_config','new')


config.add_section('dbconnection')
config.set('dbconnection', 'host','127.0.0.1')
config.set('dbconnection', 'user','root')
config.set('dbconnection', 'password','Aa*231491*dD')
config.set('dbconnection', 'database','new1')

config.add_section('configuration')
config.set('configuration', 'tablecreate_config', 'new')
config.set('configuration', 'comments', 'This is for testing purpose')

config.add_section('fixedvariables')
config.set('fixedvariables', 'us_tablename', 'user_story')
config.set('fixedvariables', 'tc_tablename', 'testcase')
config.set('fixedvariables', 'defect_tablename', 'defect')
config.set('fixedvariables', 'ustcmap_tablename', 'us_tc_map')
config.set('fixedvariables', 'tcdefectmap_tablename', 'tc_defect_map')

config.add_section('data')
config.set('data', 'us_totalcount', '10')
config.set('data', 'tc_totalcount', '20')
config.set('data', 'defect_totalcount', '10')
config.set('data', 'usp_threshold', '0')
config.set('data', 'tc_prefix', 'TC')
config.set('data', 'defect_prefix', 'D')

with open('config.ini', 'w') as config_file:
    config.write(config_file)