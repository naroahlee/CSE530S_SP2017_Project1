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
	print 'Usage: ./CropDonor.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

# Elimiate Row with Seed
City_Col    = 0
State_Col   = 1
Zip_Col     = 2
DonorID_Col = 5
PkgID_Col   = 9
ClientID    = '4002'
PkgID_BlackList = ['R150P', 'R150P1', 'R150S', 'R150S1']
DonorID_BlackList = ['', ' ']

New_List = []

isHead = True
for Item in Donor_List:
	if (True == isHead):
		New_Item = ('First name', 'Last name', 'Delivery address', 'City', 'State', 'Zip', 'DonorID', 'ClientID');
		New_List.append(New_Item)
		isHead = False
	else:
		if (isItemInList(Item[PkgID_Col], PkgID_BlackList)):
			continue
		if (isItemInList(Item[DonorID_Col], DonorID_BlackList)):
			continue
		FName = id_generator(size=6)
		LName = id_generator(size=6)
		Addr  = id_generator(size=9)
		New_Item = (FName, LName, Addr, Item[City_Col], Item[State_Col], Item[Zip_Col], Item[DonorID_Col], ClientID)
		New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
