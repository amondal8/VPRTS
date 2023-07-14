# marters-thesis
Definitional Data Description:
**1.	Code Module:** This will contain all the code modules that have been affected by the test cases. The mapping between the code modules and the test cases will be done while creating the instance data tables.

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/5fd6a618-5ede-4819-a335-55ec05904861)

**2.	Userstory:** This table contains all the user stories and their respective ids.
Primary key: us_id

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/0fc77175-bf06-4f68-b155-b30dd572f487)

Snap of the data is given below:

![image](https://github.com/amondal8/marters-thesis/assets/134355254/9e8d9f52-7851-48ef-afd9-7b92665e9992)

 
**3.	Userstoryvalue:** This table contains the user story points and the business value for the user stories. This will be mapped to the user stories while creating the instance data table.
Primary Key: None (Since the values and the combination of the values can repeat)

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/54c69f39-43c7-444f-8530-fd461286d6c8)

Sample of the data in the table is shown below:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/a291c225-b2d5-42c3-9765-fe066f61ee8f)

**4.	Testcase:** This table has the list of all the test cases. The mapping of the test cases to the user stories will be done while creating the instance data.
Primary Key: tc_id

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/dcdc68d0-1167-4340-8ed5-0ad53c26ed52)

Below is a sample of the data for this table: As of now, I have set the values for the remaining columns except for tc_id as null, we can fill up the columns as per our requirement later.

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/099cbe22-e5c6-4166-abcd-099cddd5c0f9)


**5.	Tcexectime:** This table contains the execution time for the test cases which will be mapped later while creating the instance data. All the data will be in INT format and contain time in minutes. I will import the data into the table from Excel.
Primary key: None

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/c0cda6b2-bc55-475d-98b9-18f90cb701da)

**6.	Tc_runstatus:** This table contains all the different possible status of a test case. This can be mapped to the test cases to signify the past execution results of each individual test case.
Primary Key: status_id

![image](https://github.com/amondal8/marters-thesis/assets/134355254/b851a0d4-921f-4865-ada3-c8f77b729b31)
 
Below are the possible values for this table:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/0471a834-602c-4832-8060-a9ab681bbd8f)

**7.	Tc_executionhistory:** This table will contain all the execution dates for a given test case. This table need to be organized and I may add few more columns to this table. So, this table has not yet been finalized.

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/ca327f59-38ab-415d-b23d-0ce77b07c682)

**8.	Release_data:** This table contains all the release ids with the start and end date of the release ids. This will be mapped to the user stories.
Primary key: release_id
UNIQUE: the combination of release_id, start_date and end_date has been set as a unique constraint.

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/8f1ba682-e16a-4240-b0a5-54d0d9dc69d4)

Sample of the data in the table is shown below:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/52545207-9051-42e4-af83-b84ebe64c292)

**9.	Sprint_data:** This table contains all the sprints for all the releases. This will be mapped to the user story along with the release data. The mapping of the sprint data will be done against the release data and the release data will be mapped against the user stories.
Primary key: sprint_id

![image](https://github.com/amondal8/marters-thesis/assets/134355254/bc012cd1-c501-4e37-9021-edbad22b370f)

 
Below is a sample of the data stored in the table:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/ea063f0d-2f8c-48c3-bd1e-8a5c9f6e642a)

**10.	Defect:** This table contains the list of all defects. This table will be mapped to the test case table to indicate the defects that the test cases identified in the past executions.

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/6e6e064c-5d49-4535-8e07-dbc17c9ec6a5)

The sample of the data in the table is shown below:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/0bafb095-f1fe-4bc8-95f0-62bfef3da517)

**11.	Defect_complexity:** This table contains all the possible complexities of the defects. This table has a set of predefined values identified by their ids.
Primary key: defect_complexity_id

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/78b7a70d-57d8-47af-9f11-a5a4c1183ccb)

Below are all possible values of the defect complexity:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/36d5dd9a-156c-4df7-9516-a12f0dd06841)

**12.	Defect_priority: **This table contains all the possible priorities of the defects. This table has a set of predefined values identified by their ids.
Primary Key: defect_priority_id

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/1552287d-864b-4136-83ac-ddced02d9d38)

Below are all possible values of the defect priorities:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/7278a292-04a9-40f8-b6ba-c93d31cf9624)

**13.	Defect_severity:** This table contains all the possible severities of the defects. This table has a set of predefined values identified by their ids.
Primary Key: defect_severity_id

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/3a0c3477-6cab-4b65-bd07-0e2f4288d24c)

Below are all possible values of the defect severities:
 
![image](https://github.com/amondal8/marters-thesis/assets/134355254/1078232a-2360-46a8-89d5-0960ef2769e2)

**14.	Addresource_tcexecution:** This table contains the list of all additional resources that may be needed to execute the test cases. Time will be associated with this in the tcexectime table.
Primary Key: resource_id

![image](https://github.com/amondal8/marters-thesis/assets/134355254/27a3becd-0099-4095-9b2d-0bb90b5c433c)


*_*Creating Instance data:**_

**1.	Userstory_insttable: **I have combined the userstory table, release table and the userstory value table to create the instance table for user story. 
The structure of the table:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/b9831047-6a64-4908-b74a-a7a80b08270e)

Below is the snap of the data in the table:

 ![image](https://github.com/amondal8/marters-thesis/assets/134355254/7dea2728-843b-43c9-9ed6-0a6507a3482e)

The mapping of the release id and the userstoryvalues with the user stories is done on a random manner. The user controls the number of user stories they want for the nth release(release_id = 2 in this case) and the previous releases(release_id = 1 in this case). The us_points and us_businessvalue are assigned randomly to the user stories. We can also intake other columns from the user story table, but since they are of no significance in our current implementation I have not inserted them into this instance table.


2.	Testcase_insttable: In progress creating the instance table for the test cases. 
3.	Defect_insttable: In progress creating the instance table for the defects. 

Once the instance tables are created I will do the required mapping between these tables and create the sub set of test cases that will be selected as the RTS TC set.
