#!/usr/bin/python

import sys
import csv
import time
from Getgeoid import *

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

Addr_Col    = 0
DonorID_Col = 1
Lat_Col     = 2
Lng_Col     = 3

NewList = []
#Counter = 0
for Item in Donor_List:
	# Track Process
	# Counter += 1
	# CounterStr = "\r%d" % (Counter)
	# sys.stdout.write(CounterStr)
	# sys.stdout.flush()

	# Get Coordination
	GeoID = GetGeoidGC(Item[Lat_Col], Item[Lng_Col])
	NewItem = tuple(Item) + GeoID
	
	# Join a NewTuple
	# print NewItem
	NewList.append(NewItem)
	time.sleep(2)


# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)
