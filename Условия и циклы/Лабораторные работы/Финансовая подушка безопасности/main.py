money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = -1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital >= 0:
    money_capital += salary - spend
    spend_1 = spend * 0.05
    spend += spend_1
    count += 1
    continue
else:
    print("Количество месяцев, которое можно протянуть без долгов:", count)
