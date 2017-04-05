#!/usr/bin/python

import csv
Input_CSV  = 'MergedCensus.csv'
Output_CSV  = 'MergedCensus_NoDup.csv'


# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

StateCode_Col  = 0
CountyCode_Col = 1
TractCode_Col  = 2
Year_Col       = 4

NewList = []
Entries = set()

for Item in Donor_List:

	Key = (
		Item[StateCode_Col], 
		Item[CountyCode_Col], 
		Item[TractCode_Col], 
		Item[Year_Col])
	
	if Key not in Entries:
		Entries.add(Key)
		NewList.append(Item)

# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)

