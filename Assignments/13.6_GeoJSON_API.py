import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter a Location: ")
    if len(address) < 1: break

    #obtain the REST API URL address
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms) #formats the dictionary into URL syntax

    #obtain the response
    print("Retrieving", url)
    webhandle = urllib.request.urlopen(url, context=ctx)
    data = webhandle.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failture to Retrieve ====')
        print(data)
        continue

    #in the json print the place id. path is: {[{key="place_id"}]}
    #the json returned a dictionary with 2 elements the elements keys/tags were "results", "status"
    #within the [results] element there was a list with 1 item, the item was a dictionary
    #within that dictionary there were multiple key value pairs, some with further levels of nesting, but here was "place_id"
    #print(js['results'][0]['place_id'])
    print(js['results'][0]['place_id'])
