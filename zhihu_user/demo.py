import json

with open('items.json','r') as fp:
    data = ""
    for line in fp:
        data = data + line
    s = json.loads(data)
    print(typr(s))
    print(s[1]["name"])
