# TODO реализовать функцию
def get_sentences_list(text):
    sen_list = []
    for sen in text.split("."):
        if sen:
            sen_list.append(sen.strip())
    return sen_list


print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
