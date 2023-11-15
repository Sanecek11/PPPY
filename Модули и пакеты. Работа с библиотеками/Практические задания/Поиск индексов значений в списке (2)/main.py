# TODO написать функцию index
def index(lst, value):
    list_index = [i for i, current_value in enumerate(lst) if current_value == value]
    if not list_index:
        raise ValueError("нет индекса")
    return list_index


if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
