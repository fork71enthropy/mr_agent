import requests




r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
a =r.status_code
b =r.headers['content-type']
c =r.encoding
d =r.text
e =r.json()
results = [a,b,c,d,e]

for_view = []

for i in range(len(results)):
    for_view.append(results[i])


for i in range(len(for_view)):
    print(f"{for_view[i]}\n")