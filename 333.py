import requests
# query = {
#     "inn": "6623134596"
# }
# query1 = {
#     "inn": "6623141177"
# }
# делаем запрос и получаем данные из него
# print(response1)
s1 = []
s2 = []
# print(response)
def qq():
    query = {
        "inn": "6623134596"
    }
    response = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query)
    response = response.json()
    for i in response['message']['founders']:
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
            for t in response['message']['foundersH']:
                if 'innfl' in t:
                    s1.append(t['innfl'])
                elif 'inn' in t:
                    qw = s1
            for t in response['message']['directors']:
                s1.append(t['innfl'])
            for t in response['message']['directorsH']:
                s1.append(t['innfl'])
    for i in response['message']['foundersH']:
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
            for t in response['message']['foundersH']:
                if 'innfl' in t:
                    s1.append(t['innfl'])
                elif 'inn' in t:
                    qw = s1
            for t in response['message']['directors']:
                s1.append(t['innfl'])
            for t in response['message']['directorsH']:
                s1.append(t['innfl'])
    for i in response['message']['directors']:
        s1.append(i['innfl'])
    for i in response['message']['directorsH']:
        s1.append(i['innfl'])

def ww():
    query1 = {
        "inn": "6623141177"
    }
    response1 = requests.post('https://dev.vdelo.pro/api/hackaton/kontur-focus/company/details', json=query1)
    response1 = response1.json()
    print(response1)
    for i in response1['message']['founders']:
        if 'innfl' in i:
            s2.append(i['innfl'])
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
        for t in respons['message']['foundersH']:
            if 'innfl' in t:
                s1.append(t['innfl'])
            elif 'inn' in t:
                qw = s1
        for t in response['message']['directors']:
            s1.append(t['innfl'])
        for t in response['message']['directorsH']:
            s1.append(t['innfl'])
    for i in response1['message']['foundersH']:
        if 'innfl' in i:
            s2.append(i['innfl'])
        elif 'inn' in i:
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
            for t in respons['message']['foundersH']:
                if 'innfl' in t:
                    s1.append(t['innfl'])
                elif 'inn' in t:
                    qw = s1
            for t in response['message']['directors']:
                s1.append(t['innfl'])
            for t in response['message']['directorsH']:
                s1.append(t['innfl'])
    for i in response1['message']['directors']:
        s2.append(i['innfl'])
    for i in response1['message']['directorsH']:
        s2.append(i['innfl'])
qq()
ww()
print(s1)
print(s2)
for i in s1:
    for r in s2:
        if i == r:
            print("EGEGE")
            break




