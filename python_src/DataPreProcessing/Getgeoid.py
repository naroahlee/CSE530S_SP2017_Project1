#!/usr/bin/python

import urllib
import csv
import re

# Use Geocoding
def GetGeoidGC(Lat, Lng):
	#making the url
	MyUrl = ('https://geocoding.geo.census.gov/geocoder/geographies/coordinates'
			'?x=%s'
			'&y=%s'
			'&benchmark=8&vintage=8'
			) % (Lng, Lat)
	#grabbing the JSON result
	response = urllib.urlopen(MyUrl)
	htmlsrclines = response.read().splitlines()
	for line in htmlsrclines:
		if(-1 != line.find('GEOID')):
			Infoline = line
			break
	TempLine = re.findall(r'GEOID: [0-9]{11}[^0-9]{1}', Infoline)
	StateCode  = TempLine[0][7  :  9]
	CountyCode = TempLine[0][9  : 12]
	TractCode  = TempLine[0][12 : 16] + '.' + TempLine[0][16 : 18]
	return (StateCode, CountyCode, TractCode)
