#!python3

import json, requests


url = "http://127.0.0.1:5000/post"
payload = {
    'var1'  : "some data",
    'age'   : 20,
    'money' : 15.25,
    'boolean' : True,
    'multi' : {
        'second' : 'level!'
    },
    'after' : 'nope'
}

response = requests.post(url,data=payload)
print(f"The response is {response}")
print(f"The response text is {response.text}")
data = json.loads(response.text)
print(f"The json decoded response is {data}")
for i in data:
    print(i,data[i])