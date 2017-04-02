#!/usr/bin/python
import csv
import sys

# Function Check whether an Item in a list
def isItemInList(Item, List):
	flag = False
	for Iter in List:
		if(Item == Iter):
			flag = True
			break
	return flag

# =============== Script Starts ==================

if (len(sys.argv) != 3):
	print 'ERROR: Argument'
	print 'Usage: ./CropSendMail.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

# Elimiate Row with Seed
DonorID_Col = 5
PkgID_Col   = 9
PkgID_BlackList = ['R150P', 'R150P1', 'R150S', 'R150S1']
DonorID_BlackList = ['', ' ']

New_List = []
for Item in Donor_List:
	if (isItemInList(Item[PkgID_Col], PkgID_BlackList)):
		continue
	if (isItemInList(Item[DonorID_Col], DonorID_BlackList)):
		continue
	New_Item = (Item[DonorID_Col], Item[PkgID_Col])
	New_List.append(New_Item)
	


# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
