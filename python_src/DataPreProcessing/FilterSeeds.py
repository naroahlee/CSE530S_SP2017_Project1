#!/usr/bin/python
import csv
import sys
import string
import random


# Function Check whether an Item in a list
def isItemInList(Item, List):
	flag = False
	for Iter in List:
		if(Item == Iter):
			flag = True
			break
	return flag

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

# =============== Script Starts ==================

if (len(sys.argv) != 3):
	print 'ERROR: Argument'
	print 'Usage: ./FilterSeeds.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

# Elimiate Row with Seed
Street_Col  = 10
City_Col    = 11
State_Col   = 12
Zip_Col     = 13
DonorID_Col = 16
PkgID_Col   = 20
PkgID_BlackList = ['R150P', 'R150P1', 'R150S', 'R150S1']
DonorID_BlackList = ['', ' ']

New_List = []

for Item in Donor_List:
	if (isItemInList(Item[PkgID_Col], PkgID_BlackList)):
		continue
	if (isItemInList(Item[DonorID_Col], DonorID_BlackList)):
		continue
	New_List.append(Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
