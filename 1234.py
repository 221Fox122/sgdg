import requests
a = input()
b = input()
qq1 = []
qq2 = []
qq1.append(a)
qq2.append(b)
s1 = []
s2 = []
# 6623134596
# 6623141177
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
                query2 = {
                    "inn": i['inn']
                }
                response2 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query2)
                response2 = response2.json()

                for t in response2['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response2['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response2['message']['directors']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

                for t in response2['message']['directorsH']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

        for i in response1['message']['foundersH']:
            if 'innfl' in i:
                if i['innfl'] not in s1:
                    s1.append(i['innfl'])

                query3 = {
                         "inn": i['inn']
                     }
                response3 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query3)
                response3 = response3.json()
                for t in response3['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response3['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s1:
                            s1.append(t['innfl'])

                for t in response3['message']['directors']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

                for t in response3['message']['directorsH']:
                    if t['innfl'] not in s1:
                        s1.append(t['innfl'])

        for i in response1['message']['directors']:
            if i['innfl'] not in s1:
                s1.append(i['innfl'])

        for i in response1['message']['directorsH']:
            if i['innfl'] not in s1:
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
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])
            elif 'inn' in i:
                query5 = {
                    "inn": i['inn']
                }
                response5 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query5)
                response5 = response5.json()
                for t in response5['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response5['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])

                for t in response5['message']['directors']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])
                for t in response5['message']['directorsH']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])

        for i in response4['message']['foundersH']:
            if 'innfl' in i:
                if i['innfl'] not in s2:
                    s2.append(i['innfl'])
            elif 'inn' in i:
                query6 = {
                    "inn": i['inn']
                }
                response6 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query6)
                response6 = response6.json()
                for t in response6['message']['founders']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response6['message']['foundersH']:
                    if 'innfl' in t:
                        if t['innfl'] not in s2:
                            s2.append(t['innfl'])
                for t in response6['message']['directors']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])
                for t in response6['message']['directorsH']:
                    if t['innfl'] not in s2:
                        s2.append(t['innfl'])

        for i in response4['message']['directors']:
            if i['innfl'] not in s2:
                s2.append(i['innfl'])

        for i in response4['message']['directorsH']:
            if i['innfl'] not in s2:
                s2.append(i['innfl'])


def ee():
    for o in s1:
        query7 = {
            "inn": o
        }
        response7 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query7)
        response7 = response7.json()
        for i in response7['message']['data']:
            if len(i['inn']) == 12:
                if i['inn'] not in s1:
                    s1.append(i['inn'])
            else:
                if i['inn'] not in qq1:
                    qq1.append(i['inn'])
    print(qq1)
def rr():
    for o in s2:
        query8 = {
            "inn": o
        }
        response8 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query8)
        response8 = response8.json()
        for i in response8['message']['data']:
            if len(i['inn']) == 12:
                if i['inn'] not in s2:
                    s2.append(i['inn'])
            else:
                if i['inn'] not in qq2:
                    qq2.append(i['inn'])
    print(qq2)



qq()
ww()
ee()
rr()
qq()
ww()
print(s1)
print(s2)
for i in s1:
    for r in s2:
        if i == r:
            print(i)
            exit()
# query7 = {
#     "inn": "662345141917"
# }
# response7 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/person', json=query7)
# response7 = response7.json()
# for i in response7['message']['data']:
#     (i['inn'])
# print(response7['message']['data'][])

