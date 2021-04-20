import urllib.request, urllib.parse, urllib.error
import ssl
import re
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_html(url):
    html = urllib.request.urlopen(url, context=ctx).read() #returns all the html as is (messy)
    soup = BeautifulSoup(html, 'html.parser') #cleans the html using BS4 with the html.parser argument.
    return soup

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
    urllist = list()
    for tag in get_html(url)('a'): # Needed to update your variable to new url html
        urllist.append(tag.get('href', None))
    url = (urllist[specifiedposition])

#using regex extract the name in the url
x = re.findall('by_(.+)\.html', url)
print(x.pop())
