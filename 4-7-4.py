import matplotlib.pyplot as plt

#리스트 범위(x축)
x = range(0,256)
#리스트 범위(y축)
y = []
for v in x:
    y.append(v*v)

print(y)

plt.plot(x,y,'r')
plt.show()
