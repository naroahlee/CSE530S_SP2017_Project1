#!/usr/bin/python

import csv
Input1_CSV  = 'Matched.csv'
Input2_CSV  = 'CensusNonMSA.csv'
Output_CSV  = 'MergedGeoID.csv'


NewList = []
Header = ('DonorID', 'StateCode', 'CountyCode', 'TractCode', 'MSA', 'CensusYear')
NewList.append(Header)

MyYear='2015'

# Read DonorList provided by Data Vendor
with open(Input1_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

DonorID_Col      = 1
MSA_Col          = 12
StateCode_Col    = 15
CountyCode_Col   = 17
TractCode_Col    = 14

isHead = True
for Item in Donor_List:
	if(True == isHead):
		isHead = False
		continue

	NewItem = (Item[DonorID_Col], Item[StateCode_Col], Item[CountyCode_Col], Item[TractCode_Col], Item[MSA_Col], MyYear) 
	
	# print NewItem
	NewList.append(NewItem)


with open(Input2_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)

DonorID_Col      = 0
MSA_Col          = 4
StateCode_Col    = 14
CountyCode_Col   = 17
TractCode_Col    = 13

isHead = True
for Item in Donor_List:
	if(True == isHead):
		isHead = False
		continue

	NewItem = (Item[DonorID_Col], Item[StateCode_Col], Item[CountyCode_Col], Item[TractCode_Col], Item[MSA_Col], MyYear) 
	
	# print NewItem
	NewList.append(NewItem)


# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)
