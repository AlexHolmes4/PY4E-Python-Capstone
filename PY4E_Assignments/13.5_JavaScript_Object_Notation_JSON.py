import json

data = '''
[
    {   "id" : "001",
        "x" : "2",
        "phone" : {
            "type" : "local",
            "number" : "0422 233 1233"
        },
        "name" : "Chuck"
    },
    {   "id" : "009",
        "x" : "7",
        "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
        },
        "name" : "Alex"
    }
]'''

#parse the json and present it as dictionary or list depending on json provided.
info = json.loads(data) #load string and parse into structured object, traceback with syntax errors.
print('User count', len(info))

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Phone Number Type:', item['phone']['type'], ' - ', item['phone']['number'])
    print('Attribute:', item['x'])
