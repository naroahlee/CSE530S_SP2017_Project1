#!/usr/bin/python

import sys
import csv
from Getgeo import *

if (len(sys.argv) != 3):
	print 'ERROR: Argument'
	print 'Usage: ./GetCensusFromGeocode.py [InputCSV] [OutputCSV]'
	sys.exit()

Input_CSV   = sys.argv[1]
Output_CSV  = sys.argv[2]

# Read DonorList provided by Data Vendor
with open(Input_CSV, 'r') as readFile:
	reader = csv.reader(readFile)
	Donor_List = list(reader)


MyAddr      = "6625 Clayton AVE, St. Louis, MO, 63139"
MyYear      = '2015'
MyGeoCode   = GetGeocodeFFIEC(MyAddr, MyYear)
MyCensus = GetCensusFFIEC(
			MyGeoCode['sMSACode'],
			MyGeoCode['sStateCode'], 
			MyGeoCode['sCountyCode'], 
			MyGeoCode['sTractCode'], 
			MyGeoCode['iCensusYear'])
MyCensusHeader = ExtractDict(MyCensus, 'Header')

# Elimiate Row with Seed
MSACode_Col      = 12
StateCode_Col    = 15
CountyCode_Col   = 17
TractCode_Col    = 14
Year_Col         = 3

NewList = []
isHead = True
Counter = 0
for Item in Donor_List:
	if(True == isHead):
		NewList.append(MyCensusHeader)
		isHead = False
	else:
		# Track Process
		Counter += 1
		CounterStr = "\r%d" % (Counter)
		sys.stdout.write(CounterStr)
		sys.stdout.flush()
		if(Counter >= 5000):
			break
		# Get Geocode
		TempCensus  = GetCensusFFIEC(Item[MSACode_Col], Item[StateCode_Col], Item[CountyCode_Col], Item[TractCode_Col], Item[Year_Col])
		TempData    = ExtractDict(TempCensus, 'Data')
		
		# print NewItem
		NewList.append(TempData)


# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)
