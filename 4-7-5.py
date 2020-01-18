import matplotlib.pyplot as plt
#fig 객체 생성
fig = plt.figure()
#서브 슬롯 생(2행 1열)
ax1 =fig.add_subplot(2,1,1)
ax2 =fig.add_subplot(2,1,2)


#리스트 범위(x축)
x = range(0,256)
#리스트 범위(y축)
y = []
for v in x:
    y.append(v*v)

z = []
for v in x:
    z.append(v*v)

#라인 차트(1행1열)
ax1.plot(x,y,'b',z,'r')
#바 차트(2행1열)
ax2.bar(x,z)

plt.show()
