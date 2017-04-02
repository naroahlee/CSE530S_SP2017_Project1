#!/usr/bin/python
import csv
import sys

# =============== Script Starts ==================
if (len(sys.argv) != 2):
	print 'ERROR: Argument'
	print 'Usage: ./CreateClient.py [OutputCSV]'
	sys.exit()

Output_CSV  = sys.argv[1]

New_List = []

New_Item = ('ClientType', 'ClientID', 'ClientName', 'EID')
New_List.append(New_Item)

New_Item = ('Rental', 4002, 'AXZ', 'SN9001')
New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
