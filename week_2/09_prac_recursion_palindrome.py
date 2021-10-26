# 회문 검사
# slicing 사용법 array[0:2], array[1:-2]
# :-1 하면 마지막 앞까지
input = "소주만병만주소"
print(input[1:-1])
print(input[0])
print(input[-1])


# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n - 1 - i]:
#             return False
#     return True

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])


print(is_palindrome(input))
