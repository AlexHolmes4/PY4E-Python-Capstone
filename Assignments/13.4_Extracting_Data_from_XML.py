#This program will prompt for a URL, read the XML data from that URL using urllib
#and then parse and extract the comment counts from the XML data, computing the sum of numbers in the file

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#obtain the input source
url = input('Enter URL: ')
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_42.xml"
print("Retrieving", url)

#obtain the response
webhandle = urllib.request.urlopen(url, context=ctx)
byteresp = webhandle.read()
print("Retrieved", len(byteresp), "characters")
#print(byteresp.decode()) hidden, as used for reviewing XML format prior to parsing.

#parse into ET to otain the paths
tree = ET.fromstring(byteresp) #fromstring works with class bytes

#identify all nodes that are on the path argument provided
commentNodesList = tree.findall('comments/comment')
print("Count:", len(commentNodesList))

#loop through all the nodes, and append to list if criteria met (comment node, count)
countlist = list()
for element in commentNodesList:
    strcount = element.find('count').text
    countlist.append(int(strcount)) #add data to a list
print("Sum:", sum(countlist))
