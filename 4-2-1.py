from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "C:/python/webcrolling/section4/webcrolling_section4/forcast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

# 지역 확인
info = {}
for location in soup.find_all("location"):
    if location.find('city').string == "대전":
        daejeon_loc = location.find_all('data')

for loc in daejeon_loc:
    time = loc.find("tmef").string
    weather = loc.find('wf').string
    tempL = loc.find('tmn').string
    tempH = loc.find('tmx').string
    rnst = loc.find('rnst').string
    if not (time in info):
        info[time] = []
    info[time].append(weather)
    info[time].append(tempL)
    info[time].append(tempH)
    info[time].append(rnst)

# 각 지역의 날씨 출력 (Mac window)
# with open('C:/python/webcrolling/section4/webcrolling_section4/weather.txt', "wt", encoding="utf-8") as f:
#     for loc in sorted(info.keys()):
#         print("+", loc)
#         f.write(str(loc)+'\n')
#         for name in info[loc]:
#             print(" - ", name)
#             f.write('\t'+str(name)+'\n')

# 대전지역 시간 별 날씨 출력 (Mac window)

with open('C:/python/webcrolling/section4/webcrolling_section4/daejeon_weather.txt', "wt", encoding="utf-8") as f:
    for loc in info.keys():
        print(loc)
        f.write(str(loc)+'\n')
        i = 0
        for name in info[loc]:
            if i % 4 == 0:
                print(" - ", name)
                f.write('Weather :'+str(name)+'\n')
            elif i % 4 == 1:
                print(" - ", name)
                f.write('Temp Low:'+str(name)+'\n')
            elif i % 4 == 2:
                print(" - ", name)
                f.write('Temp High:'+str(name)+'\n')
            elif i % 4 == 3:
                print(" - ", name)
                f.write('Rust:'+str(name)+'\n')
            i += 1
