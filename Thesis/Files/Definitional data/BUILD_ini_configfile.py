import configparser

config = configparser.ConfigParser()

config.add_section('tablecreation')
config.set('tablecreation', 'creation_config','new')


config.add_section('dbconnection')
config.set('dbconnection', 'host','127.0.0.1')
config.set('dbconnection', 'user','root')
config.set('dbconnection', 'password','Aa*231491*dD')
config.set('dbconnection', 'database','definitionaldata')

config.add_section('configuration')
config.set('configuration', 'tablecreate_config', 'new')
config.set('configuration', 'comments', 'This is for testing purpose')

config.add_section('tablenames')
config.set('tablenames', 'us_tablename', 'userstory')
config.set('tablenames', 'usvalue_tablename', 'userstoryvalue')
config.set('tablenames', 'releasedata', 'release_data')
config.set('tablenames', 'sprintdata', 'sprint_data')

config.set('tablenames', 'tc_tablename', 'testcase')
config.set('tablenames', 'tcrunstatus_tablename', 'tc_runstatus')
config.set('tablenames', 'tcexectime_tablename', 'tcexectime')
config.set('tablenames', 'tcexechistory_tablename', 'tc_executionhistory')

config.set('tablenames', 'defect_tablename', 'defect')
config.set('tablenames', 'defectcomplexity_tablename', 'defect_complexity')
config.set('tablenames', 'defectpriority_tablename', 'defect_priority')
config.set('tablenames', 'defectseverity_tablename', 'defect_severity')

config.set('tablenames', 'codemodule_tablename', 'code_module')

config.set('tablenames', 'ustcmap_tablename', 'us_tc_map')
config.set('tablenames', 'tcdefectmap_tablename', 'tc_defect_map')

config.add_section('data')
config.set('data', 'us_totalcount', '10')
config.set('data', 'tc_totalcount', '20')
config.set('data', 'defect_totalcount', '10')
config.set('data', 'usp_threshold', '0')
config.set('data', 'tc_prefix', 'TC')
config.set('data', 'defect_prefix', 'D')

with open('config1.ini', 'w') as config_file:
    config.write(config_file)