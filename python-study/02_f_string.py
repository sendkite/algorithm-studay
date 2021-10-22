scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}
]

for i in scores:
    name = i['name']
    score = i['score']
    print(f'{name}의 점수는 {score} 입니다')
