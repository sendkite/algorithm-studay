# 이진 탐색
# 최소값, 최대값을 더해서 반값이 검색 타겟
# 이진 탐색을 위해서는 정렬이 필요하다


finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2
    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1
        cur_guess = (cur_max + cur_min) // 2
    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
