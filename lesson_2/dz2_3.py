number_month = int(input('Введите номер месяца: '))
#1е решение
list_year = ['зима', 'весна', 'лето', 'осень']
if number_month == 1 or number_month == 2 or number_month == 12:
    print(list_year[0])
elif 3 <= number_month < 6:
    print(list_year[1])
elif 6 <= number_month < 9:
    print(list_year[2])
elif 9 <= number_month < 12:
    print(list_year[3])
else:
    print('Вы ввели неверный номер месяца')

#2е решение
dict_year = {12: 'зима', 1: 'зима', 2: 'зима',
             3: 'весна', 4: 'весна', 5: 'весна',
             6: 'лето', 7: 'лето', 8: 'лето',
             9: 'осень', 10: 'осень', 11: 'осень'}

for key in dict_year:
    if number_month == key:
        print(f'{key}й месяц: {dict_year.get(key)}')


