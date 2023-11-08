# TODO реализовать функцию count
def count(list_, n):
    c1 = list_.count(n)
    return c1

list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
