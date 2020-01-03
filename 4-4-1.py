import simplejson as json

# Dict(Json)선언
data = {}
data['people'] = []
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul',
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan'
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon'
})
# print(type(data))
# print(data)

# Dict(Json) -> str
e = json.dumps(data, indent=4)
# print(type(e))
# print(e)

# Str -> Dict(Json)
d = json.loads(e)
# print(type(d))
# print(d)

# json 파일 쓰기
with open('C:/python/webcrolling/section4/webcrolling_section4/member.json', 'w') as outfile:
    outfile.write(e)

# json 파일 읽기
with open('C:/python/webcrolling/section4/webcrolling_section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    print(type(r))
    print(r)
    for p in r['people']:
        print('Name : ', p['name'])
        print('Website : ', p['website'])
        print('From : ', p['from'])
        print("")
