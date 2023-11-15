number = 2342354235235

list_digits = digits_list = [int(d) for d in str(number)]  # приводим каждый символ к числу
# TODO c помощью list comprehension получить список цифр числа

print(sum(digits_list))  # TODO найти сумму цифр числа
print(sum(d for d in digits_list if d % 2 == 0))  # TODO найти сумму всех четных чисел
print(len(digits_list))  # TODO найти количество цифр
print(min(digits_list))  # TODO найти минимальную цифру
print(digits_list[0] - digits_list[-1])  # TODO найти разность между первой и последней цифрой
