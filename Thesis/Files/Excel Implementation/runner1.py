import time
import numpy as np
import openpyxl as op
import random
import contextualComparison_final as cc
import matrixcreation as matc
import creatingsubsets as subsets
import defectmapping as defmapping

filepath = "/Thesis/Files/Mapping.xlsx"
total_uscount = 10
total_tccount = 20
connection_prob = 1   # Using a value less than 1 will decrease the 1s even more, so use it wisely
limiting_ones_tcmat = 8
worksheetname_tc_userstory = "Req_Mapping_Rev"

# Defect subset creation variables
defect_count=10
connection_prob_defectmat = 1
defect_minlimit = 0
defect_maxlimit = 3

cc.texualcomparison()   # Textual comparison of the user stories of current sprint with suer stories of previous sprints

adj_matrix = matc.generate_random_adjmat_withlimits(total_uscount,total_tccount,connection_prob,limiting_ones_tcmat)    # Creating the adjacency matrix for mapping of user stories to test cases
print(adj_matrix)
matc.writematto_reqmappingexcel(adj_matrix)     # Printing the TC to user story adjacency matrix on to the excel, "Row=User stories; Column=Test cases"
matc.writeto_revReqMat_excel(adj_matrix)    # Printing the TC to user story adjacency matrix on to the excel, "Row=Test Cases; Column=User stories"

workbook = op.load_workbook(filepath)
worksheet_tccount = workbook[worksheetname_tc_userstory]
tc_count = worksheet_tccount.max_row    # Counting the total number of test cases present

defectmap_adjmat = defmapping.generate_defectmap_adjmat_withlimits(tc_count,defect_count, connection_prob_defectmat, defect_minlimit, defect_maxlimit)  # Creating the adjacency matrix for mapping defects to test cases
print(defectmap_adjmat)
defmapping.writematto_defectmappingexcel(defectmap_adjmat)  # Writing the defect mapping adjacency matrix to excel

