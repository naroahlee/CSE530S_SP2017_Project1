#!/usr/bin/python

import sys
import csv

if (len(sys.argv) != 2):
	print 'ERROR: Argument'
	print 'Usage: ./CropDonor.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Out1_CSV    = 'Matched.csv'
Out2_CSV    = 'NonMatched.csv'


# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

Status_Col = 18

MatchedList    = []
NonMatchedList = []
isHead = True
for Item in Donor_List:
	if(True == isHead):
		MatchedList.append(Item)
		NonMatchedList.append(Item)
		isHead = False
	else:
		if ('Y' == Item[Status_Col]):
			MatchedList.append(Item)
		else:
			NonMatchedList.append(Item)

with open(Out1_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(MatchedList)

with open(Out2_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NonMatchedList)
