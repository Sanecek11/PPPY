total = 0

while True:
    number = input("Введите число (или 'stop' для завершения): ")  # Запрашиваем первое следующее числа в цикле

    if number == "stop":
        break

    total += int(number)  # Суммируем число с общей суммой

print("Сумма чисел:", total)  # Выводим общую сумму
print("Конец программы")
