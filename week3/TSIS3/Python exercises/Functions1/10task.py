def unique_list(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst
input_list = [1, 2, 1, 2, 3, 3, 4, 5, 6, 4, 7, 8, 3, 9, 7, 8, 9]
output_list = unique_list(input_list)
print(output_list)
