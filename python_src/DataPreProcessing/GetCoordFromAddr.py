#!/usr/bin/python

import sys
import csv
from Getlatlng import *

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


NewList = []
isHead = True
Counter = 0
for Item in Donor_List:
	if(True == isHead):
		NewItem = ('Address', 'DonorID', 'Lat', 'Lng')
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

		Addr = Item[Addr_Col]
		MailboxPos = Addr.index(",")
		Addr = Addr[MailboxPos + 1:]
		# Get Coordination
		Coord = GetLatLngOG(Addr)
		NewItem = (Addr, Item[DonorID_Col]) + Coord
		
		# Join a NewTuple
		#print NewItem
		NewList.append(NewItem)


# Dump CSV File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(NewList)
