people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        if person['age'] < 20:
            print(person['name'])
    except:  # 왠만하면 안쓰는 것이 좋다
        print(person['name'], '에러입니다')

# 팁: 파일 분리 from * import *
