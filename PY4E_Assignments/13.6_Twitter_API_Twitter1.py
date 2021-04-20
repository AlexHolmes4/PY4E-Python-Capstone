import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

#created an app https://developer.twitter.com/en/portal/apps
#added the consumer keys, and authentication tokens into hidden.property

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

#Ignore the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders()) #gets a dictionary of the headers
    # print headers
    print('Remaining',headers['x-rate-limit-remaining'])
