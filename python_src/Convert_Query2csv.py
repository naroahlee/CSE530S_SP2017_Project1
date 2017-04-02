#!/usr/bin/python
# Convert Query Result to CSV

import sys
import csv
import psycopg2


if (len(sys.argv) != 5):
	print 'ERROR: Argument'
	print 'Usage: ./Convert_Query2csv.py [DBName] [Username] [InputSQL] [OutputCSV]'
	sys.exit()

# Setup Parameter from Commandline
DBName      = sys.argv[1]
username    = sys.argv[2]

Input_SQL   = sys.argv[3]
Output_CSV  = sys.argv[4]

# ================ Connect DB and Run Query ================
# Start A Query Session
ConnPara   = 'dbname=' + DBName + ' ' + 'user=' + username
RetList = []

# Connect The DB
conn = psycopg2.connect(ConnPara)

# Create aa Cursor Based on an opened connection
cur = conn.cursor()

cur.execute(open(Input_SQL, "r").read())

RetList = cur.fetchall()

# Close and Disconnect
cur.close()
conn.close()
# ==========================================================

# Dump CSV File to a new File
with open(Output_CSV, 'w') as resFile:
	writer = csv.writer(resFile, dialect = 'excel')
	writer.writerows(RetList)
