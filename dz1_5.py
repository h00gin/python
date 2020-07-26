proceeds = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))

if proceeds > costs:
    print(f'Ваша прибыль составила: {proceeds-costs}')
else:
    print (f'Ваш убыток составил: {-(proceeds-costs)}')

numberWorkers = int(input('Введите численность сотрудников: '))
if proceeds > costs:
    print(f'Прибыль в расчете на одного сотрудника составила: {(proceeds-costs)//numberWorkers}')
else:
    print(f'Убыток в расчете на одного сотрудника составила: {-((proceeds - costs) / numberWorkers)}')
