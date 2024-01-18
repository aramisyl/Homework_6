values = input("Введите список чисел").split(", ")


def min_and_max(values):
    test_list = [int(i) for i in values]
    test_list_sorted = sorted(test_list)
    min = test_list_sorted[0]
    max = test_list_sorted[-1]
    return f'Минимальное значение {min}, максимальное значение {max}.'


print(min_and_max(values))
