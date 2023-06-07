import requests
query = {
    "inn": "6623134596"
}
query1 = {
    "inn": "6623141177"
}
# делаем запрос и получаем данные из него
response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
response = response.json()
response1 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query1)
response1 = response1.json()
# print(response1)
s1 = []
s2 = []
# print(response)
for i in response['message']['founders']:
    if 'innfl' in i:
        s1.append(i['innfl'])
    elif 'inn' in i:
        s1.append(i['inn'])
for i in response['message']['foundersH']:
    if 'innfl' in i:
        s1.append(i['innfl'])
    elif 'inn' in i:
        s1.append(i['inn'])
for i in response['message']['directors']:
    s1.append(i['innfl'])
for i in response['message']['directorsH']:
    s1.append(i['innfl'])

for i in response1['message']['founders']:
    if 'innfl' in i:
        s2.append(i['innfl'])
    elif 'inn' in i:
        s2.append(i['inn'])
for i in response1['message']['foundersH']:
    if 'innfl' in i:
        s2.append(i['innfl'])
    elif 'inn' in i:
        s2.append(i['inn'])
for i in response1['message']['directors']:
    s2.append(i['innfl'])
for i in response1['message']['directorsH']:
    s2.append(i['innfl'])
for i in s1:
    for r in s2:
        if i == r:
            print("EGEGE")
            break
