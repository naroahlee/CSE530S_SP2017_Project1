#!/usr/bin/python
import csv
import sys

# =============== Script Starts ==================
if (len(sys.argv) != 2):
	print 'ERROR: Argument'
	print 'Usage: ./CreateCampaign.py [OutputCSV]'
	sys.exit()

Output_CSV  = sys.argv[1]

New_List = []

New_Item = ('ProjectID', 'CampaignID', 'CampaignDate', 'CampaignType', 'ClientID')
New_List.append(New_Item)

New_Item = (2871, 'R15', '1/1/15', 'House', 4002)
New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
