import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter URL Address: ")
webhandle = urllib.request.urlopen(url)
data = webhandle.read().decode()
print("Retrieved", len(data), "characters")
print("Count:", len(json.loads(data)['comments'])) #added this to get the count: as per 13.6 assignemnt req. 

#parse the unicode through json loads and identify the array sub to loop through,
#for each cycle take the key count and change it to an int to allow sum function to work.
print("Sum:", sum([int(comment['count']) for comment in (json.loads(data))['comments']]))
