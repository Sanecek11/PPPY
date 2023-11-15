# TODO Напишите функцию decimal_to_hex
def decimal_to_hex():
    return {i: hex(i) for i in range(0, 16)}

if __name__ == '__main__':
    ...  # TODO Распечатайте словарь с десятичными и шестнадцатеричными числами
dict_ = decimal_to_hex()
print(dict_)