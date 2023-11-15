
def is_lucky_number(num: int) -> bool:
    ...  # TODO проверить что число шестизначное и положительное
    if num < 0:
        raise ValueError("число не является положительным")
    if len(str(num)) != 6:
        raise ValueError("число не является шестизначным")
    ...  # TODO проверить счастливое число или нет
    list_d = [int(d) for d in str(num)]
    return sum(list_d[:3]) == sum(list_d[3:])

print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
