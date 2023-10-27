salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
months_1 = 10
increase = 0.03  # Ежемесячный рост цен
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
while months_1:
    spend = spend + (0 if months_1 == 10 else spend * 0.03)
    money_capital += spend - salary
    months_1 -= 1
else:
    print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital, 2))
