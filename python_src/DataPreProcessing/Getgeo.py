#!/usr/bin/python

import requests

def GetGeocodeFFIEC(AddressLine, Year):
	url = "https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetGeocodeData"
	params = {
		'sSingleLine': AddressLine, 
		'iCensusYear': Year}
	r = requests.post(url, json=params)
	jsonData = r.json()
	return jsonData['d']


def GetCensusFFIEC(MSACode, StateCode, CountyCode, TractCode, Year):
	url = "https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetCensusData"
	params = {
			'sMSACode'    : MSACode,
			'sStateCode'  : StateCode,
			'sCountyCode' : CountyCode,
			'sTractCode'  : TractCode,
			'iCensusYear' : Year
			}
	r = requests.post(url, json=params)
	jsonData = r.json()
	return jsonData['d']

def GetCensusFFIEC2(StateCode, CountyCode, TractCode, Year):
	url = "https://geomap.ffiec.gov/FFIECGeocMap/GeocodeMap1.aspx/GetCensusDataNoMSA"
	params = {
			'sStateCode'  : StateCode,
			'sCountyCode' : CountyCode,
			'sTractCode'  : TractCode,
			'iCensusYear' : Year
			}
	r = requests.post(url, json=params)
	jsonData = r.json()
	return jsonData['d']

def ExtractDict(Dict, Type):
	if ('Header' == Type):
		Pos = 0
	elif ('Data' == Type):
		Pos = 1
	else:
		return ()
	
	TempTuple = ()
	for Item in Dict.iteritems():
		if ('ExtensionData' == Item[0]):
			continue
		TempTuple = TempTuple + (Item[Pos],)
	return TempTuple

