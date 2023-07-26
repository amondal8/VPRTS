import configparser

config = configparser.ConfigParser()
config.read('config1.ini')
run_config = config['run_configuration']

import config_initialsetup
if run_config["run_config"].lower() == "copy" and run_config["copy_ds_id"].lower() == "yes":
    print("config1")
    import final_implementation
else:
    print("config2")
    import fill_datasettables
    import fill_mappingtables
    import final_implementation