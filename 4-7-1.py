from pandas import Series

#Series1 선언
series1 = Series([123,234,345,456,567])
print(series1)
# 총 개수
print(series1.count())
# 요약
print(series1.describe())
# 인덱스 접근
print(series1[2])

#Series1 선언
series2 = Series([123,234,345,456,567],index=['2018-02-12','2018-02-13','2018-02-14','2018-02-15','2018-02-16'])
print(series2)

#인덱스 순회
for data in series2.index:
    print(data)

#값 순회
for price in series2.values:
    print(price)

#series3 선언
series_g1 = Series([10,20,30],index=['n1','n2','n3'])
series_g2 = Series([50,20,10],index=['n3','n2','n1'])

#Series 병합 & 계산
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1 * series_g2) * (0.5 + 1)

print(sum)
print(mul)
print(cul)
