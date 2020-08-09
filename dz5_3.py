with open('text_3.txt', 'r', encoding='utf-8') as test_fail:
    sum_workers = 0
    sum_wage = 0
    print('Сотрудники с заработной платой больше 20000 руб:')
    for line in test_fail:
        line = line.split()
        line[1] = float(line[1])
        if line[1] > 20000:
            print(line[0])
        if line != '\n':
            sum_workers += 1
        sum_wage += line[1]
    avarage_wage = sum_wage / sum_workers

    print(f'Средняя заработная плата сотрудников равна: {avarage_wage}')
