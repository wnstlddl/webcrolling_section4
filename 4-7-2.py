from pandas import Series, DataFrame
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding = 'utf-8')

r_data = {'City':['서울','대구','대전','부산'],'Total':[567,345,456,567],'Total2':[333,444,555,666]}
i_data = ['one','two','three','four']

#출력1
print(r_data)
print(i_data)

#DataFrame 정의
d_frame = DataFrame(r_data,index=i_data)
# print(type(d_frame))
# print(d_frame)
# print(d_frame.index)
# print(d_frame.values)
# print(d_frame['City']) # 열 가져오기
# print(d_frame.ix['one']) # 행 데이터 가져오기
# print(type(d_frame.ix['one'])) # 시리즈임

#값 순회

for e in d_frame.values:
    for i,z in enumerate(e):
        print(i,z)
