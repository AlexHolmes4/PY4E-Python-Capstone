import urllib.request, urllib.parse, urllib.error
from urllib.request import Request
from bs4 import BeautifulSoup
import ssl  #a module that provides access to Transport Layer Security - commonly known as the Secure Sockets Layer

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("please provide a URL: ")
req = Request(url, headers={'User-Agent': 'Alakazam/over9000'}) #provides a known browser agent to work around 403 Forbidden error (security on host)
html = urllib.request.urlopen(req, context=ctx).read() #the string is passed into the url request, and turned to bytes, a socket made and the response found, then it's read() to a long string with new lines /n at the end of each line
soup = BeautifulSoup(html, 'html.parser') #Creating a soup object, by passing the url and the argument of what to do with it / how to clean it up we chose html.parser

#Retrieve all of the anchor tags
tags = soup('a') #passing paramater into the newly created soup object named soup, to find every occurance of 'a'
for tag in tags:
    print(tag.get('href', None)) #finds 'a' in the string, and looks for a href if none found returns none, otherwise returns the href
