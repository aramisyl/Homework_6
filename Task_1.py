def greatest_common_divisor(a, b):
    if a > b:
        divider = b
        divisible = a
    else:
        divider = a
        divisible = b

    while divisible % divider > 0:
        remainder = divisible % divider
        if remainder > 0:
            divisible = divider
            divider = remainder
    return divider


print(greatest_common_divisor(24, 18))
