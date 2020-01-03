# a = 'hello'
# print(type(a))
# print(a[0])
# print(a[0:3])
# print(a[-1:])
# for t in a:
#     print(type(t))

# 리스트 자료형 (순서,중복,수정,삭제 모두 가능)

# 선언
a = []
b = list()
c = [0, 0, 1, 2]
d = [0, 1, 'car', [1, 2, 3, 4]]

# 연산
print(d[0:3])
print(c+d)
print(c*3)

# 리스트 수정 삭제
c[1] = 5
print(c)
c[1:2] = ['a', 'b', 'c']
print(c)
c[1] = ['a', 'b', 'c']
print(c)
del c[1]
print(c)

# 리스트 함수
a = [9, 4, 3, 4, 5]
a.append(7)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.count(4))
print(a)
print(a.pop())
print(a)
# 리스트 삭제 : del, remove, pop

while a:
    ls = a.pop()
    print(ls == 4)
