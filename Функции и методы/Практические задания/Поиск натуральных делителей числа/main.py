def get_list_number_divisors(number):
    ...  # TODO Найдите список делителей числа number
    list_of_dev = []
    for num in range(1, number + 1):
        if number % num == 0:
           list_of_dev.append(num)
    return list_of_dev

print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
