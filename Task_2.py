table = []

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        value = i * j
        row.append(value)
        j += 1
    table.append(row)
    i += 1

print(table)

table_2 = []
m = 1

while m <= 10:
    n = 1
    row = []
    while n <= 10:
        value = m * n
        row.append(value)
        n += 1
    table_2.append(row)
    m += 1

print(table_2)
