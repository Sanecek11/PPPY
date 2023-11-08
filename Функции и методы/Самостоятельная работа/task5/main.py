# TODO реализовать функцию
def get_sentences_list(text):
    # list_ = [(text.split(".")).strip([])] """ .strip не работает со списком"""
    # (text.split(".")).strip([])
    list_ = str(text.split("."))
    return list_


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
