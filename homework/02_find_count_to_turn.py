input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    arry = ""
    for i in string:
        if i == "0":
            arry += i
        else:
            arry += "0"
    return arry


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
