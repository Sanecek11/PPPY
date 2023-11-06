# TODO Напишите функцию find_common_items
def find_common_items(last_week, current_week):
    purchases = list(set(last_week).intersection(set(current_week)))
    purchases.sort()
    return purchases


last_week_items = ['книга', 'ноутбук', 'флешка', 'мышь']
current_week_items = ['ноутбук', 'флешка', 'наушники', 'монитор']

print(f"Общие товары: {find_common_items(last_week_items, current_week_items)}")  # TODO Распечатайте общие товары
