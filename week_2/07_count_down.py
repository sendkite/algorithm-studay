# 재귀함수
# 무한 루프에 빠지지 않도록 항상 탈출 조건을 작성해 준다.

def count_down(number):
    if number < 0:
        return
    print(number)  # number를 출력하고
    count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다!



count_down(60)
