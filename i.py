from random import *

'''
data=list()
for i in range(10):
    data.append(randint(1,100))

def insert_sort(data):
    for i in range(len(data)):
        key=data[i] #맨 처음값
        for j in range(i,0,-1):
            if key < data[j-1]:
                data[j-1],data[j]=data[j],data[j-1]
            else:
                break
    return data

print(insert_sort(data))

def insert_sort(li):
    for i in range(len(li)):
        key=li[i]
        for j in range(i,0,-1):
            if key < li[j-1]:
                li[j-1],li[j]=li[j],li[j-1]
    print(li)
    print(li[8])

insert_sort(li)


li=[]
for i in range(10):
    li.append(randint(1,1000))

li.sort()
print(li)
print(li[8])


def fac(num):
    if num > 1:
        return num*(num-1)
    else:
        return num

for i in range(5):
    print(fac(i))




a=[]
N=randint(1,10)
for i in range(N):
    a.append(randint(1,10))
a.sort()
k=len(a)


a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(a+b)



data=[4,1,2,5,9]
left=[]
right=[]
pivot=data[0]

for i in range(1,5):
    if pivot > data[i]:
        left.append(data[i])
    else:
        right.append(data[i])

print(left)
print(right)
print(left+pivot+right)


import random
data=random.sample(range(100),10)

def quick_sort(data):
    if len(data)<=1:
        return data

    left = []
    right = []
    pivot = data[0]

    for i in range(1,len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else :
            right.append(data[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(data))




s=input()
for i in s.split(","):
    print(i.strip("[]"),end='')




dict={'book':'책',  'apple':'사과',  'candy':'사탕'}
k=[i for i in dict.keys()]
v=[j for j in dict.values()]
print(k)
print(v)


class Area:
    def set(self,d1,d2,d3):
        self.d1=d1
        self.d2=d2
        self.d3=d3

    def get(self):
        return self.d1*self.d2

a1=Area()
a2=Area()
a1.set(10,6,'red')
a2.set(4,4,'blue')
print(a1.get())
print(a2.get())

import queue
data=queue.Queue()
print(type(data))



import random

li=random.sample(range(100),10)
print(li)

li.sort()
print(li)


a=[[10,20],
   [30,40],
   [50,60]]

for i in a:
    for j in i:
        print(j, end=' ')
    print()


li=[]
for i in range(3):
    li1=[]
    for j in range(3):
        li1.append(10)
    li.append(li1)
print(li)

li=[[10 for j in range(3)] for i in range(3)]
print(li)

##sorted : 리스트 정렬
stu=[['gyuri','jaewoo','']]

stu=[['gyuri','B',95],
    ['jaewoo','A',90],
    ['haemin','C',100]]



g=dict()  #g={'A':['B','C'],    }

g['A']=['B','C']
g['B']=['A','D']
g['C']=['A','G','H','I']
g['D']=['B','E','F']
g['E']=['D']
g['F']=['D']
g['G']=['C']
g['H']=['C']
g['I']=['C','J']
g['J']=['I']

print(g)

def dfs(g, start):
    visited, will=list(),list()
    will.append(start)

    while will:
        node=will.pop()
        if node not in visited:
            visited.append(node)
            will.extend(g[node])

    return visited
print(dfs(g,'A'))

'''

def recur(li):
    if len(li)==1:
        return li
    return li[-1:] + recur(li[:-1])

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li=recur(li)
print(li)

a =reversed(li)
print(list(a))








