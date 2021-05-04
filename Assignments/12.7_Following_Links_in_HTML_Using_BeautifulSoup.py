#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Breandan.html

import urllib.request, urllib.parse, urllib.error
import ssl
import re
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("please enter a URL: ")

while True:
    try:
        specifiedposition = int(input('Enter a position that crawler should navigate to: '))-1
        break
    except:
        print("Error: please provide a numerical count")
        continue
while True:
    try:
        specifiedcount = int(input('Enter a count for how deep the crawler should go: '))
        break
    except:
        print("Error: please provide a numerical count")
        continue

for i in range(specifiedcount): #alternative to iterating count flag value

    #take the last url value given and clean up the html
    html = urllib.request.urlopen(url, context=ctx).read() #returns all the html as is (messy)
    soup = BeautifulSoup(html, 'html.parser') #cleans the html using BS4 with the html.parser argument.

    #Retrieve all of the anchor tags from the html
    listoflinks = list()
    tags = soup('a') #returns line after line of anchor tags. #tags is class = bs4.elemement.resultset
    for tag in tags: #iterates through the results set, each iteration is class = bs4.element.tag
        listoflinks.append(tag.get('href', None))# the get method called on the bs4.element.tag object allows for arguments such as 'href' which pulls the URL portion, if not found returns None.

    #return the link thats 3rd on the list, and navigate to that link next cycle.
    #print("ive gone down",count,"times")  #for testing
    url = (listoflinks[specifiedposition])

#using regex extract the name in the url
x = re.findall('by_(.+)\.html', url)
print(x.pop())
