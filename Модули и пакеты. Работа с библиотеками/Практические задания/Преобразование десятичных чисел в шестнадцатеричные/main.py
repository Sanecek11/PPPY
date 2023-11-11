# TODO Напишите функцию decimal_to_hex
def decimal_to_hex() -> dict[int, str]:
    return {k: hex(k) for k in range(16)}

if __name__ == '__main__':
    ...  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
converted_dict = decimal_to_hex()
print(converted_dict)
