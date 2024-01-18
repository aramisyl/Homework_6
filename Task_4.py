def max_of_row(values):
    max_list = []
    for row in values:
        max_list.append(max(row))
    return max_list


print(max_of_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
