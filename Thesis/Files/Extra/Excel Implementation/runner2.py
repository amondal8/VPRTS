import time
import numpy as np
import openpyxl as op
import random
import contextualComparison_final as cc
import matrixcreation as matc
import creatingsubsets as subsets
import defectmapping as defmapping


filepath = "/Thesis/Files/Mapping.xlsx"
usp_threshold=0
total_executiontime = 89  # execution window time in minutes
fixed_tcexecutiontime = 15    # fixed execution time of each test case in minutes
worksheetname_executiontime = "TC_Executiontime"


# Calling methods from creatingsubsets.py
list = subsets.creation_userstorysubsets(usp_threshold)  # Creating the list of user stories based on the set threshold
tc_set = subsets.creation_testcasesubset(list)  # Creating the subset of test cases based on the selected user stories (contains all the user stories whose USP values are more than the set threshold)
sorted_tcdict = subsets.creationof_prioritydict(tc_set)     # Creating a sorted list of the above selected test cases based on the user story points of the user stories they are effecting
subsets.creatingtcset_fixedexecutiontime(sorted_tcdict, total_executiontime, fixed_tcexecutiontime)     # Creating a smaller subset of test cases based on a fixed execution time for each test case
tcexec_dict = subsets.createdictfromexcel(filepath, worksheetname_executiontime, 1, 2)  # Creating a dictionary where TC# is the key and its execution time is the value
subsets.creatingtcset_varyingecutiontime(sorted_tcdict, total_executiontime, tcexec_dict)   # Creating a smaller subset of test cases based on the variable exacution time for each test case

# Calling methods from defectmapping.py
defect_subset = defmapping.creation_defectsubset(tc_set)    # Creating the subset of defects that gets identified by the selected subset of test cases

defect_dict = defmapping.creation_defectdict()  # Creation of dictionary with TC as key and list of defects as value
defmapping.defect_issubset(defect_dict, defect_subset)  # Creating the subset of test cases that get affected due to the subset of defects

