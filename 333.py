import requests
a = input()
b = input()
qq1 = []
qq2 = []
qq1.append(a)
qq2.append(b)
s1 = []
s2 = []
def qq():
    for k in range(len(qq1)):
        query1 = {
            "inn": qq1[k]
        }
        response1 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query1)
        response1 = response1.json()
        for i in response1['message']['founders']:
            if 'innfl' in i:
                s1.append(i['innfl'])
            elif 'inn' in i:
                qw = s1
                query2 = {
                    "inn": i['inn']
                }
                response2 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query2)
                response2 = response2.json()
                for t in response2['message']['founders']:
                    if 'innfl' in t:
                        s1.append(t['innfl'])
                    elif 'inn' in t:
                        return
                for t in response2['message']['foundersH']:
                    if 'innfl' in t:
                        s1.append(t['innfl'])
                    elif 'inn' in t:
                        qw = s1
                for t in response2['message']['directors']:
                    s1.append(t['innfl'])
                for t in response2['message']['directorsH']:
                    s1.append(t['innfl'])
        for i in response1['message']['foundersH']:
            if 'innfl' in i:
                s1.append(i['innfl'])
            elif 'inn' in i:
                qw = s1
                query3 = {
                         "inn": i['inn']
                     }
                response3 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query3)
                response3 = response3.json()
                for t in response3['message']['founders']:
                    if 'innfl' in t:
                        s1.append(t['innfl'])
                    elif 'inn' in t:
                        return
                for t in response3['message']['foundersH']:
                    if 'innfl' in t:
                        s1.append(t['innfl'])
                    elif 'inn' in t:
                        qw = s1
                for t in response3['message']['directors']:
                    s1.append(t['innfl'])
                for t in response3['message']['directorsH']:
                    s1.append(t['innfl'])
        for i in response1['message']['directors']:
            s1.append(i['innfl'])
        for i in response1['message']['directorsH']:
            s1.append(i['innfl'])

def ww():
    for k in range(len(qq2)):
        query4 = {
            "inn": qq2[k]
        }
        response4 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query4)
        response4 = response4.json()
        for i in response4['message']['founders']:
            if 'innfl' in i:
                s2.append(i['innfl'])
            elif 'inn' in i:
                query5 = {
                    "inn": i['inn']
                }
                response5 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query5)
                response5 = response5.json()
                for t in response5['message']['founders']:
                    if 'innfl' in t:
                        s2.append(t['innfl'])
                    elif 'inn' in t:
                        return
                for t in response5['message']['foundersH']:
                    if 'innfl' in t:
                        s2.append(t['innfl'])
                    elif 'inn' in t:
                        qw = s1
                for t in response5['message']['directors']:
                    s2.append(t['innfl'])
                for t in response5['message']['directorsH']:
                    s2.append(t['innfl'])
        for i in response4['message']['foundersH']:
            if 'innfl' in i:
                s2.append(i['innfl'])
            elif 'inn' in i:
                query6 = {
                    "inn": i['inn']
                }
                response6 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query6)
                response6 = response6.json()
                for t in response6['message']['founders']:
                    if 'innfl' in t:
                        s2.append(t['innfl'])
                    elif 'inn' in t:
                        return
                for t in response6['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                    elif 'inn' in t:
                        qw = s1
                for t in response6['message']['directors']:
                    s2.append(t['innfl'])
                for t in response6['message']['directorsH']:
                    s2.append(t['innfl'])
        for i in response4['message']['directors']:
            s2.append(i['innfl'])
        for i in response4['message']['directorsH']:
            s2.append(i['innfl'])



# qq()
# ww()
print(s1)
print(s2)
for i in s1:
    for r in s2:
        if i == r:
            print("EGEGE")
            exit()
query7 = {
    "inn": "662345141917"
}
response7 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query7)
response7 = response7.json()
for i in response7['message']['data']:
    print(i['inn'])
# print(response7['message']['data'][])

