# TODO Напишите функцию calculate_average_age для расчета среднего возраста студентов
def calculate_average_age(students_dict):
    return sum(students_dict.values()) / len(students_dict)
students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}
print(f"Средний возраст студентов: {calculate_average_age(students_dict)}")  # TODO Распечатайте средний возраст студентов
