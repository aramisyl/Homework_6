input = input("Введите список чисел с кратным количеством элементов.").split(", ")


def calculate_column_sum(input):
    # Валидация ввода
    if len(input) % 2 != 0:
        print("Список элементов не кратный.")

    if len(input) % 2 == 0:
        # Трансформация списка чисел в двухмерный массив
        old_list = [int(i) for i in input]
        middle_element = int(len(old_list) / 2)
        pt_1 = list(old_list[0:middle_element])
        pt_2 = list(old_list[middle_element:])
        new_list = [pt_1, pt_2]

        # Pacчет суммы столбцов
        sum_list = [0 in range(len(new_list[0]))]
        for i in range(len(new_list)):
            for j in range(len(new_list[i])):
                sum_list[j] += new_list[i][j]

        return sum_list


print(calculate_column_sum(input))
