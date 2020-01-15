import pandas as pd

df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx')

#컬럼 값 수정
# df['State'] = df['State'].str.replace(' ','|')
# print(df)

#평균 컬럼 추가
df['Avg'] = df[['2003','2004','2005']].mean(axis=1).round(2)
print(df)

df['Sum'] = df[['2003','2004','2005']].sum(axis=1).round(2)
print(df)

#최대값
df['max'] = df[['2003','2004','2005']].max(axis=1)
print(df)
print(df[['2003','2004','2005']].max(axis=0))

#최소값
df['min'] = df[['2003','2004','2005']].min(axis=1)
print(df)
print(df[['2003','2004','2005']].min(axis=0))

#상세정보 한번에 보기

print(df.describe())

df.to_excel('C:\python_Webcroling\section4\ re_excel_s1.xlsx',index=None)
