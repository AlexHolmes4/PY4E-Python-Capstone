import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

#created an app https://developer.twitter.com/en/portal/apps
#added the consumer keys, and authentication tokens into hidden.property

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

#Ignore the SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders()) #gets a dictionary of the headers
    print('\n','Remaining',headers['x-rate-limit-remaining'])

    for u in js['users']:
        print(u['screen_name'])
        if 'status' not in u:
            print('   * No status found')
            continue
        s = u['status']['text']
        print('   ', s[:120])
