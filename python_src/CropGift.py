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
	print 'Usage: ./CropGift.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Gift_List = list(reader)

# Elimiate Row with Seed
GDate_Col   = 1
GType_Col   = 5
GID_Col     = 3
GState_Col  = 15
GAmount_Col = 2
DonorID_Col = 13
PkgID_Col   = 9

New_List = []
for Item in Gift_List:
	while ',' in Item[GAmount_Col]:
		Item[GAmount_Col] = Item[GAmount_Col].replace(',', '')
	New_Item = (Item[GDate_Col], Item[GType_Col], Item[GID_Col], Item[GState_Col], Item[GAmount_Col], Item[DonorID_Col], Item[PkgID_Col])
	New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
