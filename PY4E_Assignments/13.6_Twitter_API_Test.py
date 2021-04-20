import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

#created an app https://developer.twitter.com/en/portal/apps
#added the consumer keys, and authentication tokens into hidden.property

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
            {'screen_name' : 'drchuck', 'count' : '2'})
print(url)

#Ignore the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

headers = dict(connection.getheaders()) #gets a dictionary of the headers
print(headers)
