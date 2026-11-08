def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]

    numbers = range_of_numbers(start_num, end_num -1 )
    numbers.append(end_num)
    return numbers

print(range_of_numbers(4, 7))   # [4, 5, 6, 7]