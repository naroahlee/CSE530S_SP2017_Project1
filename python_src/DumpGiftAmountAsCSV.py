#!/usr/bin/python

import csv
import psycopg2

DBName = 'Fund_Raising'
username = 'yehanspc'
ConnPara = 'dbname=' + DBName + ' ' + 'user=' + username

MyQueryFile = './GetGiftAmountofCampaign.sql'

RetList = []
AmountList = []

# Connect The DB
conn = psycopg2.connect(ConnPara)

# Create aa Cursor Based on an opened connection
cur = conn.cursor()

cur.execute(open(MyQueryFile, "r").read())

RetList = cur.fetchall()

# Close and Disconnect
cur.close()
conn.close()

for TupleItem in RetList:
	AmountList.append(TupleItem[0])

# Dump CSV File to a new File
with open('GiftAmountInCSV.csv', 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(RetList)
