#a.json파일 만들기
import json

with open('a.json', 'w') as f:
    json.dump('hi', f)

with open('a.json') as f:
    a=json.load(f)
    print(a)





