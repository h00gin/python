with open('text_5.txt', 'w') as list_number:
    try:
        numbers = input('Введите цифры, разделенные пробелом: ')
        list_number.writelines(numbers)
        sum_num = 0
        numbers = numbers.split()
        for number in numbers:
            if number != ' ' and number != '\n':
                sum_num += int(number)
        print(f'Сумма цифр в файле равна: {sum_num}')
    except ValueError:
        print('Строка должна состоять только из цифр')

