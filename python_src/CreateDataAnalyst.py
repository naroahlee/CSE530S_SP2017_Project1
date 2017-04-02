#!/usr/bin/python
import csv
import sys

# =============== Script Starts ==================
if (len(sys.argv) != 2):
	print 'ERROR: Argument'
	print 'Usage: ./CreateDataAnalyst.py [OutputCSV]'
	sys.exit()

Output_CSV  = sys.argv[1]

New_List = []

New_Item = ('EID', 'Fname', 'Lname', 'Gender', 'DOB')
New_List.append(New_Item)

New_Item = ('SN9001', 'Yao', 'Wang' , 'F', '4/2/89')
New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
