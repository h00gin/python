name = input('Введите свое имя: ')

surname = input('Введите свою фамилию: ')

age = int(input('Введите свой возраст: '))

age_program = int(input('Какой у вас опыт программирования: '))

print(name, surname, '{} лет. Опыт программирования: {}'.format(age, age_program))
print(type(name))
print(type(surname))
print(type(age))
print(type(age_program))

