#!/usr/bin/python
import urllib
import urllib2

#with open('./MyKey.key', 'r') as rdfile:
#    AUTH_KEY = rdfile.read()

AUTH_KEY='lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24'
url = 'https://www.mapquestapi.com/geocoding/v1/address?key=%s' % (AUTH_KEY)
#url = 'http://open.mapquestapi.com/geocoding/v1/address?key=%s' % (AUTH_KEY)
#LocStr = "PO Box 343, Leverett, MA 01054"
#LocStr = "6625 Clayton AVE, St. Louis, MO, 63139"

print url
values = {"options":{},"location":{"street":"PO Box 343","city":"Leverett","state":"MA","postalCode":"01054","adminArea1":"US"}}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
