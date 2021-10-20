def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        index_array = ord(char) - ord("a")
        alphabet_occurrence_array[index_array] += 1

        max_num = alphabet_occurrence_array[0]
        for num in alphabet_occurrence_array:
            if num > max_num:
                max_num = num
        return chr(max_num + ord("a"))


print(find_alphabet_occurrence_array("hello my name is sparta"))
