#!/usr/bin/python

from Getgeo import *


MyAddr = "6625 Clayton AVE, St. Louis, MO, 63139"
MyYear = '2015'

MyGeoCode = GetGeocodeFFIEC(MyAddr, MyYear)



#print MyGeoCode['sMatchAddr']
#print MyGeoCode['sLatitude']
#print MyGeoCode['sLongitude']
#print MyGeoCode['sMSACode']
#print MyGeoCode['sStateCode']
#print MyGeoCode['sCountyCode']
#print MyGeoCode['sTractCode']

MyCensus = GetCensusFFIEC(
			MyGeoCode['sMSACode'],
			MyGeoCode['sStateCode'], 
			MyGeoCode['sCountyCode'], 
			MyGeoCode['sTractCode'], 
			MyGeoCode['iCensusYear'])
	


#print MyCensus

MyGeoHeader = ExtractDict(MyGeoCode, 'Header')
MyGeoData   = ExtractDict(MyGeoCode, 'Data')
print MyGeoHeader
print MyGeoData

MyCensusHeader = ExtractDict(MyCensus, 'Header')
MyCensusData   = ExtractDict(MyCensus, 'Data')
print MyCensusHeader
print MyCensusData

MyCensus2 = GetCensusFFIEC2(
			MyGeoCode['sStateCode'], 
			MyGeoCode['sCountyCode'], 
			MyGeoCode['sTractCode'], 
			MyGeoCode['iCensusYear'])
MyCensusHeader2 = ExtractDict(MyCensus2, 'Header')
MyCensusData2   = ExtractDict(MyCensus2, 'Data')
print MyCensusHeader2
print MyCensusData2
