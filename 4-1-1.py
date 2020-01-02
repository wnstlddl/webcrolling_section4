import pickle  # (객체,텍스트)직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = 'C:/python_Webcroling/section4/test1.bin'
tfilename = 'C:/python_Webcroling/section4/test2.txt'

data1 = 77
data2 = "Hello, world!"
data3 = ['car', 'apple', 'house']

# 파이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f)  # dumps (문자영 직렬화)
    pickle.dump(data2, f)
    pickle.dump(data3, f)

# 텍스트 쓰기
with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))  # 리스트 형태 순서대로 써주는것, 리스트는 걍은 안됨

# 바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f)  # loads (문자열 역직렬화)
    print(type(b), ' Binart Read1 :', b)
    b = pickle.load(f)
    print(type(b), ' Binart Read2 :', b)
    b = pickle.load(f)
    print(type(b), ' Binart Read3 :', b)

with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), 'Text read' + str(i) + "|", line, end='')
