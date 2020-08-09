with open('text_2.txt', 'r', encoding='utf-8') as test_fail:
    line_count = 0
    words_count = 0
    for line in test_fail:
        if line != '\n':
            line_count += 1
        line = line.split()
        words_count += len(line)

    print(f'Количество строк в файле равно: {line_count}')
    print(f'Количество слов в файле равно: {words_count}')
