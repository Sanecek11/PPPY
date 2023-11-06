# TODO реализовать функцию
def get_unique_words(str_):
    sw = list(set(str_.split()))
    sw.sort()
    return sw
print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
