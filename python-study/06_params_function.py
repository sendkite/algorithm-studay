# 매개변수 인자 기본 지정하기

def cal(a, b=2):
    return a + 2 * b


result = cal(1)
print(result)

# *args 넣으면 매개변수 무한으로 넣을 수 있음
# **kwargs 매개변수로 딕셔너리를 넣을 수 있음


