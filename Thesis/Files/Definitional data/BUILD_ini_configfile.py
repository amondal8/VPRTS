import configparser

config = configparser.ConfigParser()

config.add_section('dbconnection')
config.set('dbconnection', 'host','127.0.0.1')
config.set('dbconnection', 'user','root')
config.set('dbconnection', 'password','Aa*231491*dD')
config.set('dbconnection', 'database','definitionaldata')

config.add_section('dbconnection_dataset')
config.set('dbconnection_dataset', 'host','127.0.0.1')
config.set('dbconnection_dataset', 'user','root')
config.set('dbconnection_dataset', 'password','Aa*231491*dD')
config.set('dbconnection_dataset', 'database','dataset_schema')

config.add_section('tablenames')
config.set('tablenames', 'us_tablename', 'userstory')
config.set('tablenames', 'usvalue_tablename', 'userstoryvalue')
config.set('tablenames', 'releasedata', 'release_data')
config.set('tablenames', 'sprintdata', 'sprint_data')
config.set('tablenames', 'tc_tablename', 'testcase')
config.set('tablenames', 'tcrunstatus_tablename', 'tc_runstatus')
config.set('tablenames', 'tcexectime_tablename', 'tcexectime')
config.set('tablenames', 'tcexechistory_tablename', 'tc_executionhistory')
config.set('tablenames', 'addresource_tablename', 'addresource_tcexecution')
config.set('tablenames', 'defect_tablename', 'defect')
config.set('tablenames', 'defectcomplexity_tablename', 'defect_complexity')
config.set('tablenames', 'defectpriority_tablename', 'defect_priority')
config.set('tablenames', 'defectseverity_tablename', 'defect_severity')
config.set('tablenames', 'codemodule_tablename', 'code_module')

#Dataset table names:

config.set('tablenames', 'dataset_tablename', 'dataset')
config.set('tablenames', 'usdatasettable_tablename', 'userstory_datasettable')
config.set('tablenames', 'tcdatasettable_tablename', 'tc_datasettable')
config.set('tablenames', 'defectdatasettable_tablename', 'defect_datasettable')
config.set('tablenames', 'cmdatasettable_tablename', 'cm_datasettable')
config.set('tablenames', 'ustcmap_tablename', 'us_tc_map')
config.set('tablenames', 'uscmmap_tablename', 'us_cm_map')
config.set('tablenames', 'tcdefectmap_tablename', 'tc_defect_map')


config.add_section('run_configuration')
config.set('run_configuration', 'run_config', 'new')        #Values set to "new" or "copy"
config.set('run_configuration', 'config_copiedfrom', 'null')    #When value of "run_config" is set to "copy"
config.set('run_configuration', 'copy_ds_id', 'yes')
config.set('run_configuration', 'matrix_build_config_uscm', 'even')   #even or composite distribution
config.set('run_configuration', 'matrix_build_configtype_uscm', 'center')    #center, Leftbound, rightbound, lefttop, righttop, leftbottom, rightbottom
config.set('run_configuration', 'matrix_build_config_tcdefect', 'even')   #even or composite distribution
config.set('run_configuration', 'matrix_build_configtype_tcdefect', 'center')    #center, Leftbound, rightbound, lefttop, righttop, leftbottom, rightbottom
config.set('run_configuration', 'matrix_build_configtype_ustc', 'even')    #center, top, bottom, even

config.add_section('data')
config.set('data', 'importanceval_calconfig', '1')      #Values can be 1 or 2
config.set('data', 'project_id', '1')
config.set('data', 'usp_threshold', '0')
config.set('data', 'us_totalcount', '20')
config.set('data', 'uscount_r1', '10')
config.set('data', 'uscount_r2', '10')
config.set('data', 'cm_totalcount', '10')
config.set('data', 'tc_totalcount', '40')
config.set('data', 'defect_totalcount', '10')
config.set('data', 'usp_threshold', '0')
config.set('data', 'tc_prefix', 'TC')
config.set('data', 'defect_prefix', 'D')
config.set('data', 'release1', '1')
config.set('data', 'release2', '2')
config.set('data', 'limiting_ones', '6')
config.set('data', 'similarityval_threshold', '.80')
config.set('data', 'total_executiontime', '90')
config.set('data', 'tcexectime_fixed', '15')
config.set('data', 'tcdefect_map_probthreshold', '.7')
config.set('data', 'uscm_map_probthreshold', '.7')


with open('config1.ini', 'w') as config_file:
    config.write(config_file)