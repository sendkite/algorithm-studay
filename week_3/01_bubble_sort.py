# 버블 정렬, 배열 요소의 앞 뒤 숫자를 비교한다. 뒤에가 더 작으면 교환
# 교환은 a,b = b,a 를 사용한다

input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!