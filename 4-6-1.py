import pandas as pd
#xlrd, openpyxl 설치 필요

#기본 읽기1
# df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx')
#sheet 순서대로 0,1,2,3,....
# df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx',sheet_name=0)
# print(df)
# print(df.head())
# print(df.tail())

#행, 푸터(Footer) 스킵
# print(df)
# df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx',skiprows=[0],skipfooter=10)

#해더 정의(1)
# df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx',header=0)
# print(df)
# print(list(df))
# print(list(df.columns.values))

#해더정의(2)
# df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx',skiprows=[0],header=None,names=['State',2003,2004,2005])
# print(list(df))
# print(list(df.columns.values))

#특정 값 치환
# df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx',na_values='...',converters={"2003": lambda w: w if w >60000 else None})
# print(df)
# print(pd.isnull(df))

#실습 정리 및 인덱스 재정의
df = pd.read_excel('C:\python_Webcroling\section4\excel_s1.xlsx')
print(df.rename(index=lambda x:x+1))
print(df.rename(index=lambda x:x+1).index)
