g_num = int(input())  # 입력 값
if g_num < 100:  # 조건 100 미만 정수
    num = g_num
    count = 0  # 사이클 수
    while True:
        # 1의 자의 10의 자리 나눠서 더한 값
        num1 = num % 10  # 1의 자리 ex) 26이면 6  8
        num2 = num // 10  # 10의 자리 ex) 26이면 2   6
        sum_number = num1 + num2  # 합 ex) 2 + 6 = 8   14

        # 10의 자리가 오른쪽 상수인 num2, 1의  합의 1의 자리
        new_num1 = sum_number % 10
        new_num2 = num1 * 10
        new_sum_number = new_num1 + new_num2

        count += 1
        if new_sum_number == g_num:
            break
        num = new_sum_number
    print(count)
else:
    print("100보다 작은 정수 입력하세요")
