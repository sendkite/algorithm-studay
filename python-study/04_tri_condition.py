num = 3

result = ('짝수' if num % 2 == 0 else '홀수')

print(f'{num}은 {result}입니다.')

# 반복문 for문 축약하기
list = [1, 3, 2, 5, 1, 2]
new_list = [i * 2 for i in list]
print(new_list)