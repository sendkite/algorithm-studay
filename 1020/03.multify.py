num1 = int(input())
num2 = int(input())

num1_one = num1 % 10
num2_one = num2 % 10

result = num1_one * num2_one

num1_two = (num1 // 10) % 10
num2_two = (num2 // 10) % 10

result2 = num1_two * num2_two

num1_thr = num1 // 100
num2_thr = num2 // 100

result3 = num1_thr * num2_thr

num2_one * num1_one
num2_one * num1_two
num2_one * num1_thr




