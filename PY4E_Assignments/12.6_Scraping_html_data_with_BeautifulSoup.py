# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1096070.html (Sum ends with 32)

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser") #all the html cleaned up in class object BeautifulSoup
tags = soup('span') #returns all the span classes #this object takes paramater of tags

#prints the sum of all the numbers on the webpage.
#Cycles through the span tags contents and coverting to an int (as .contents makes the value a navigable string)
#appends each int value to a list
#prints it's sum
#intlist = list()
#for tag in tags:
#    if re.search('[0-9]+', tag.contents[0]): #added this as an extra, as for this we only wanted to count the numbers.-
    # - every span contents was just a number but this helps to check. if they were number char mix we'd use the findall and extract we regex.
#        tag = int(tag.contents[0])
#        intlist.append(tag)
#print(sum(intlist))

print(sum([int(tag.contents[0]) for tag in soup('span')])) #same as above commented out, but with list comprehension
