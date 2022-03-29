import pygal

from a import Dice

dice=Dice()

res=[]
for i in range(100):
    result=dice.roll() #주사위 100번 던지기
    res.append(result)

fre=[]
for j in range(1, dice.num+1):
    freq=res.count(j)
    fre.append(freq)

b=pygal.Bar()
b.title="Result"
b.x_labels=['1','2','3','4','5','6']

b.add('Dice',fre)
b.render_to_file('dice.svg')














