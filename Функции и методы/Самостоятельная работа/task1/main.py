# TODO реализовать функцию
def remove_whitespace(text):
    sl = text.split(" ")
    no_spaces_list = []
    for word in sl:
        if word:
            no_spaces_list.append(word)
    return " ".join(no_spaces_list)

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
