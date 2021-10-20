input = "hello my name is sparta"


# 문자인지 확인 str.isalpha(), python chart to ASCH CODE
def find_max_occurred_alphabet(string):
    alphabet_occurred_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurred_array[arr_index] += 1
    return alphabet_occurred_array


result = find_max_occurred_alphabet(input)
print(result)
