import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''
#print("input type:",type(input),"input contains:", input)
stuff = ET.fromstring(input)
#print("stuff type:",type(stuff),"stuff contains:", stuff)
lst = stuff.findall('users/user')
#print("lst type:",type(lst),"lst contains:", lst)
print("User count: ", len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
