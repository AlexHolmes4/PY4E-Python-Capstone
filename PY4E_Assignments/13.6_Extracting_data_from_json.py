import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter URL Address: ")
webhandle = urllib.request.urlopen(url)
data = webhandle.read().decode()
print("Retrieved", len(data), "characters")

#js is a dictionary object
js = json.loads(data)
print("count:", len(js['comments']))

#append each iteration of the comments array to list and sum the int values
list = []
for comment in js['comments']:
    list.append(int(comment['count']))
print(sum(list))

#for a cleaner version (5 lines of code become 1, see 13.6-adaptation)
