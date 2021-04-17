import xml.etree.ElementTree as ET
data = '''
<stuff>
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
#print("data type:",type(data),"data contains:", data)
tree = ET.fromstring(data)
#print("tree type:",type(tree),"tree contains:", tree)
users = tree.findall('users/user')
#print("users type:",type(users),"users contains:", users)
print("User count: ", len(users))
for child in users:
    print('Name', child.find('name').text)
    print('Id', child.find('id').text)
    print('Attribute', child.get("x"))
