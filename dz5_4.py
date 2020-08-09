with open('text_4.txt', 'r') as test_file, open('text_4_rus.txt', 'w', encoding='utf-8') as new_file:
    for line in test_file:
        line = line.split()
        line_new = input(f'Введите русский перевод слова {line[0]}: ')
        new_file.write(f'{line_new} {line[1]} {line[2]} \n')
