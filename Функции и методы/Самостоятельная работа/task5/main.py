# TODO реализовать функцию
def get_sentences_list(text):
    list_ = []
    for sen in text.split("."):
        if sen:
            list_.append(sen.strip())
    return list_


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
