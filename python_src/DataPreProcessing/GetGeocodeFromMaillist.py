#!/usr/bin/python

import sys
import csv
from Getgeo import *

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


MyAddr      = "6625 Clayton AVE, St. Louis, MO, 63139"
MyYear      = '2015'
MyGeoCode   = GetGeocodeFFIEC(MyAddr, MyYear)
MyGeoHeader = ExtractDict(MyGeoCode, 'Header')

Street_Col  = 10
City_Col    = 11
State_Col   = 12
Zip_Col     = 13
DonorID_Col = 16

NewList = []
isHead = True
Counter = 0
for Item in Donor_List:
	if(True == isHead):
		NewItem = ('Address', 'DonorID') + MyGeoHeader
		NewList.append(NewItem)
		isHead = False
	else:
		# Track Process
		Counter += 1
		CounterStr = "\r%d" % (Counter)
		sys.stdout.write(CounterStr)
		sys.stdout.flush()
		if (Counter >= 5000):
			break
		# Format Address
		Address = Item[Street_Col] + ',' + Item[City_Col] + Item[State_Col] + ',' + Item[Zip_Col]
		# Get Geocode
		TempGeoCode = GetGeocodeFFIEC(Address, MyYear)
		TempData    = ExtractDict(TempGeoCode, 'Data')
		
		# Join a NewTuple
		NewItem = (Address, Item[DonorID_Col]) + TempData
		# print NewItem
		NewList.append(NewItem)


# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)
