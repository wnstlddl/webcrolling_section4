import pandas as pd

# df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv')
# print(df)

# 원치 않는 행 스킵해서 가져오는
# df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv',skiprows=[0,1])
# print(df)

#해더 지정 X
# df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv',skiprows=[0],header=None)
# print(df)

#해더 수동으로 지정
# df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015])
# print(df)

# #인덱스 컬럼 정의
# df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015],index_col=[0])
# print(df)

#특정 값 치환
# df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015],index_col=[0],na_values=['JAN'])
# print(df)

#실습 정리 및 인뎃스 재정의
# print(df)
df = pd.read_csv('C:\python_Webcroling\section4\csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015])
# print(df.index)
# print(list(df.index))
# print(df.index.values.tolist())
# print(df.index.values)
# print(df.rename(index={0:'aa',1:'bb',2:'cc'}))
# print(df.rename(index=lambda x:x+1))

#읽기

df2 = pd.read_csv('C:\python_Webcroling\section4\csv_s2.csv',sep=';',skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])
# print(df2)

#특정값 변경
# df2['Grade'] = df2['Grade'].str.replace('C','A++')
# print(df2)

#평균 컬럼 추가
df2['Avg'] = df2[['Test1','Test2','Test3','Final']].mean(axis=1)
# print(df2)

#합계 컬럼 추가
df2['sum'] = df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)
