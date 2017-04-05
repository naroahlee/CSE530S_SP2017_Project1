#!/usr/bin/python
import urllib
import urllib2
import json

#with open('./MyKey.key', 'r') as rdfile:
#    AUTH_KEY = rdfile.read()

#AUTH_KEY='lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24'
#url = 'http://open.mapquestapi.com/geocoding/v1/address?key=%s' % (AUTH_KEY)

# Use Open Geocode
def GetLatLngOG(Address):
	AUTH_KEY='lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24'
	url = 'https://www.mapquestapi.com/geocoding/v1/address?key=%s' % (AUTH_KEY)
	values = {"options":{},"location":Address}
	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()
	JsonData = json.loads(the_page)
	LatLng = JsonData['results'][0]['locations'][0]['latLng']
	return (str(LatLng['lat']), str(LatLng['lng']))
	
