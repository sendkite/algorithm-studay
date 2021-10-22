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


def check_adult(person):
    if person['age'] > 20:
        return '성인'
    else:
        return '청소년'


# people을 하나하나 풀어서 함수에 넣어라
result = map(check_adult, people)
print(list(result))

# 람다식으로 바꾸기
result = map(lambda person: "성인" if person['age'] > 20 else '청소년', people)
print(list(result))

# filter
result = filter(lambda x: x['age'] > 20, people)
print(list(result))
