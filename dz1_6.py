first_day = 2
number_day = 1

while first_day < 10:
    number_day += 1
    first_day += 0.1 * first_day
    if 3 < first_day < 4:
        print(f'Спортсмен достиг результата более 3км на {number_day}й день')
        break


