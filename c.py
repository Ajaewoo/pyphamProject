import csv
from matplotlib import pyplot as plt
from datetime import datetime
'''
filename='weather.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    #next()함수에 reader객체 넘기면 그 파일의 다음 '행'을 반환
    #print(header_row)

    #for i, j in enumerate(header_row):
    #   print(i, j)

    d,h,l=[],[],[]

    for i in reader:
        dd=datetime.strptime(i[0],"%Y-%m-%d")
        d.append(dd)

        high=int(i[1])
        h.append(high)

        low=int(i[3])
        l.append(low)

fig=plt.figure(dpi=130)
plt.plot(d,h, c='red')
plt.plot(d,l, c='blue')
plt.fill_between(d,h,l,facecolor='red',alpha=0.5)

plt.show()
'''
x=['apple', 'orange', 'lemon', 'lime']
y=[10, 15, 5, 20]
plt.subplot(131)
plt.bar(x,y)
plt.subplot(132)
plt.scatter(x,y)
plt.subplot(133)
plt.plot(x,y)

plt.show()

fruit={'apple':10, 'orange':15, 'lemon':5, 'lime':20}
name=list(fruit.keys())
value=list(fruit.values())

fig,n=plt.subplots(1,3,figsize=(8,3), sharey=True)
n[0].bar(name,value)
n[1].scatter(name,value)
n[2].plot(name,value)

fig.suptitle('Categorical')
plt.show()












