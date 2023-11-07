# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=","):
    list_people = list(set(first.split(separator)).intersection(set(second.split(separator))))
    list_people.sort()
    return list_people


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
