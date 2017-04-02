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

if (len(sys.argv) != 3):
	print 'ERROR: Argument'
	print 'Usage: ./CropDonor.py [InputCSV] [OutputCSV]'
	sys.exit()

# =============== Script Starts ==================
Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Package_List = list(reader)

# Elimiate Row with Seed
PkgID_Col      = 7
PkgRecency_Col = 4
PkgRange_Col   = 5
PkgMS_Col      = 6
ProjectID_Col  = 0
PkgID_BlackList = ['R150P', 'R150P1', 'R150S', 'R150S1']

New_List = []
for Item in Package_List:
	if (isItemInList(Item[PkgID_Col], PkgID_BlackList)):
		continue
	New_Item = (Item[PkgID_Col], Item[PkgRecency_Col], Item[PkgRange_Col], Item[PkgMS_Col], Item[ProjectID_Col])
	New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
