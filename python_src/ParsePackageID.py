#!/usr/bin/python

import csv
import sys

if (len(sys.argv) != 3):
	print 'ERROR: Argument'
	print 'Usage: ./ParsePackageID.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Rate_List = list(reader)

# Elimiate Row with Seed
PkgID_Col  = 0
Snd_Col    = 1
Rcv_Col    = 2

RecencyDig = 3
RangeDig   = 4

New_List = []
isHead = True
for Item in Rate_List:
	PkgID = Item[PkgID_Col]
	RecencyLevel = ord(PkgID[RecencyDig]) - ord('A') + 1

	New_Item = (Item[PkgID_Col], Item[Snd_Col], Item[Rcv_Col], RecencyLevel, PkgID[RangeDig])
	New_List.append(New_Item)

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(New_List)
