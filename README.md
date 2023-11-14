# MS-thesis: A value-preserving approach to RTS in Agile Methods.

Anyone willing to use this work should email and get a confirmation from: Aniruddha Mondal: amondal8@asu.edu or Dr. Kevin Gary: kgary@asu.edu

This thesis focuses on prioritizing existing user stories based on the textual similarity with new user stories and the business values before selecting the associated test cases for regression test selection (RTS) process. **Follow the folder "Definitional data" to access all the required files.**

The results of this thesis (.xlsx), my thesis writeup (pdf) and the .sql file containing the created database can be found in : **Thesis/Files/Definitional data/Additional Files**

## Understanding the Database:
The user stories have been extracted from the TAWOS dataset (https://github.com/SOLAR-group/TAWOS) and the remaining data have been synthesized. We have used two schemas while creating the data and storing the results. Below are the specifications of the schemas:

**1. Definitionaldata:** This schema is used to store the initial data before creating any specific datasets.
   The below table shows the datatables, their purpose and the fields used.
   
![image](https://github.com/amondal8/marters-thesis/assets/134355254/ad395068-1676-426f-93f5-40665cb5da5f)



**2. Dataset_schema:** This schema is used to store datasets created from the data in definitionaldata schema. These are used to run the simulations.
   The below table shows the datatables, their purpose and the fields used.
 
![image](https://github.com/amondal8/marters-thesis/assets/134355254/cd99c488-6d21-4b84-bbb3-3effbfee6198)


The field names are self explanatory but the filed names of dataset table may be hard to understand. Below table explains the purpose of each field in the **dataset table**.

![image](https://github.com/amondal8/marters-thesis/assets/134355254/17aa129e-314c-43f0-980a-0f86961fc901)



## Understanding the Codebase:

**1. Creating the tables:**
All the tables for both the schemas have been created using our python codes. This action can also be done without the use of any programming code using MySQLWorkbench (https://www.mysql.com/products/workbench/) or any similar tool. Below is the table to showcase the python files used and their purpose:

![image](https://github.com/amondal8/marters-thesis/assets/134355254/3474cedf-32da-495e-9ef6-494176540f9b)



**2. Filling the tables with data:**

   **a. Filling the tables of definitionaldata schema:**
   The extracted user stories from the TAWOS dataset are imported into our _"userstory"_ table. The data are manually extracted from the TAWOS database into an excel and then the code is run to import the data to our table. The test case ids are also imported into  the _"testcase"_ table from an excel. Methods filling data into additional tables can be ignored for the purpose of this thesis and have been placed for future use.

![image](https://github.com/amondal8/marters-thesis/assets/134355254/c876baae-6cc8-4080-862f-d599164a9ae8)

 **b. Filling the tables of datset_schema:**
 This involves three major parts: 
 
**(i) Creating dataset id:** Creating a record in the dataset table with a unique id to fill data into table specific to each dataset id.


![image](https://github.com/amondal8/marters-thesis/assets/134355254/47ec6afc-9d72-4e6a-9af9-e435fc8e6f58)


**(ii) Filling up the _userstory_datasettable_ and _tc_datasettable_:** Data from the userstory and testcase tables are fetched and filled into the _userstory_datasettable_ and _tc_datasettable_ respectively specific to every dataset id based on the user procvided input (count of user stories in each release and count of test cases, for a given dataset). The user inputs can be provided using the configuration file or the data.py file based on the requirement.

![image](https://github.com/amondal8/marters-thesis/assets/134355254/19f4b434-15f0-4a1f-b261-cb044817ad1d)


**(iii) Mapping user stories to test cases:** An adjacency matrix is created based on the total number of user stories and test cases available for a given dataset id to create a mapping. This mapping is then stored to _us_tc_map_ table specific to every dataset id.

![image](https://github.com/amondal8/marters-thesis/assets/134355254/d3464e4b-4d7e-4552-b719-96c01fdab9c9)

**3. Running the Simulations:**
Once the data have been created and pushed to the tables in accordance to specific datasets (ds_id) the final simulation is run. Running the final file produces the results specific to every dataset and the results are stored into the dataset table of dataset_schema. Along with storing the results to the database they are also exported to the desired excel into specific columns. The results in the excel are used to visulaize the results and dive deeper into analyzing them. 


![image](https://github.com/amondal8/marters-thesis/assets/134355254/83adea86-9317-4fd5-a0db-1d53f48a6fb7)


Understanding the methods of final_implementation1.py
Below table describes all the methods used in final_implementation.py in details:

![image](https://github.com/amondal8/marters-thesis/assets/134355254/010d269c-385d-4c86-be8f-2bf56997319f)

## Running the Simulations:

There are two ways in which the simulations can be run for thsi thesis using the provided codes:

**1. Process1:** The simuations should be run using this process when you are building everything from scratch and non of the schemas are setup yet. This process may take longer time to be run than process 2 as it alos involves all the initial setup of the database.

**2. Process2:** This is a suggested process if the definitionaldata schema is set and both the tables of this schema is filled with the initial data of user stories and test cases. This is a easier process and does not involve and configuration file. All the input data are fed through data.py file.

### Process 1:
   
**Steps to be followed to run the simulations using process 1:**

The above processes have been mentioned in a chronological order which has to be followed in order to run the simulations and replicate the results of this thesis. Following are the steps revisited for better understanding.

**Step1:** Extract the textual content (user story description) from the TAWOS dataset and place it on an .xlsx file which will be used to import these to our database.

**Note:** _Prerequisite for Step2 and Step3:_ The schemas need to be created manually in the database and updated in the "createTables.py" and "createInstanceTables.py" files.

**Step2:** Run the createTables.py to create the tables in "definitionaldata" schema (if not already created).

**Step3:** Run the createInstanceTables.py to create the tables in "dataset_schema" schema (if not already created).

**Step4:** Run the fill_primarytable.py to fill in data to the tables "userstory" and "testcases" of the "definitionaldata" schema. These data are extracted from the .xlsx file mentioned in Step1 and imported to our database.

**Step5:** Run the config_initialsetup.py to create a new dataset id corresponding to which the follwoing data will be created. This creates a new id everytime it is run.

**Step6:** Run the fill_datasettable.py to categorize the user stories into releases and fills in the "userstory_datasettable" table. The count of user stories in each release is user defined and can be changed for each release. This also imports the user defined count of test cases into the "tc_datasettable" table. All the data are imported from "userstory" and "testcases" tables of the "definitionaldata" schema.

**Step7:** Run the fill_mappingtable to map the user stories to test cases and store them in the "us_tc_map" table.

**Step8:** Once all the tables are filled run the final_implementation1.py to fetch the results onto the dataset table and the desired .xlsx file.

Following the above steps should provide the results using our RTS approach.

### Process 2: **(Recommended process)**

**Pre-requisites:**

1. All the tables should already created in their respective schemas.

2. Both the tables (userstory, testcase) in definitionaldata schema should already be filled with the required data.

**Steps to be followed to run the simulations using process 2:**

**Setting up the input data:**

1. All the input data should be provided to the data.py file. The variable "data" is a list of lists which takes in the input data from the user. The structure of the data variable should be [[List 1], [List 2],...,[List n]].
2. Each list should have the following data in the given order: dataset id, # of user stories for prior release, # of user stories for current release, # of code modules, # of test cases, # of defects. The description of each data is shown in the below table:

![image](https://github.com/amondal8/masters-thesis/assets/134355254/5d6b8cc4-7af4-451a-bdf7-3a6b49962dbe)

3. To run the "finalimplementation1.py" the data should be set for the variables dsid_list, exec_window and importanceval_calconfig in the data.py file. The details of these variables have been provided in the below table:

![image](https://github.com/amondal8/masters-thesis/assets/134355254/5d40773d-0c44-44cd-9986-320c250bc4bd)

The configuration terms used in the program is different from that used in the thesis. Below is the table to understand the corresponding terms:

![image](https://github.com/amondal8/masters-thesis/assets/134355254/3eb5125f-fca9-4bf1-81c2-1b2900e6b4dd)


**Execution:**

Once the input data are set, the following steps should be followed to generate the results

**Step1:** Run the "runner1.py" file. This creates a dataset using the provided dataset id (has to be unique) and fills up the following tables: "userstory_datasettable", "tc_datasettable". This also sets the business value for each user story using a random function which has right skewed distribution.

**Step2:** Run the "runner2.py" file. This fills up the "us_tc_map" table based on an adjacency matrix which is computed everytime this file is run.

**Step3:** Run the "finalimplementation1.py" file. This will compute the results and store it in the dataset table against each dataset id and also export the reults to the desired .xlsx file. The file name and path for exporting the results can be controlled using the variable "filepath_saveresults" from the "utilities_dataset.py" file

Following the above steps should provide the results using our approach.
