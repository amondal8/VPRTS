# marters-thesis
Definitional Data Description:
1.	Code Module: This will contain all the code modules that have been affected by the test cases. The mapping between the code modules and the test cases will be done while creating the instance data tables.
 
2.	Userstory: This table contains all the user stories and their respective ids.
Primary key: us_id
 
Snap of the data is given below:
 
3.	Userstoryvalue: This table contains the user story points and the business value for the user stories. This will be mapped to the user stories while creating the instance data table.
Primary Key: None (Since the values and the combination of the values can repeat)
 
Sample of the data in the table is shown below:
 
4.	Testcase: This table has the list of all the test cases. The mapping of the test cases to the user stories will be done while creating the instance data.
Primary Key: tc_id
 
Below is a sample of the data for this table: As of now, I have set the values for the remaining columns except for tc_id as null, we can fill up the columns as per our requirement later.
 

5.	Tcexectime: This table contains the execution time for the test cases which will be mapped later while creating the instance data. All the data will be in INT format and contain time in minutes. I will import the data into the table from Excel.
Primary key: None
 
6.	Tc_runstatus: This table contains all the different possible status of a test case. This can be mapped to the test cases to signify the past execution results of each individual test case.
Primary Key: status_id
 
Below are the possible values for this table:
 
7.	Tc_executionhistory: This table will contain all the execution dates for a given test case. This table need to be organized and I may add few more columns to this table. So, this table has not yet been finalized.
 
8.	Release_data: This table contains all the release ids with the start and end date of the release ids. This will be mapped to the user stories.
Primary key: release_id
UNIQUE: the combination of release_id, start_date and end_date has been set as a unique constraint.
 
Sample of the data in the table is shown below:
 
9.	Sprint_data: This table contains all the sprints for all the releases. This will be mapped to the user story along with the release data. The mapping of the sprint data will be done against the release data and the release data will be mapped against the user stories.
Primary key: sprint_id
UNIQUE: the combination of sprint_id, start_date and end_date has been set as a unique constraint.
 
Below is a sample of the data stored in the table:
 
10.	Defect: This table contains the list of all defects. This table will be mapped to the test case table to indicate the defects that the test cases identified in the past executions.
 
The sample of the data in the table is shown below:
 
11.	Defect_complexity: This table contains all the possible complexities of the defects. This table has a set of predefined values identified by their ids.
Primary key: defect_complexity_id
 
Below are all possible values of the defect complexity:
 
12.	Defect_priority: This table contains all the possible priorities of the defects. This table has a set of predefined values identified by their ids.
Primary Key: defect_priority_id
 
Below are all possible values of the defect priorities:
 
13.	Defect_severity: This table contains all the possible severities of the defects. This table has a set of predefined values identified by their ids.
Primary Key: defect_severity_id
 
Below are all possible values of the defect severities:
 

