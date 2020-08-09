with open('text_1.txt', 'w', encoding='utf-8') as test_fail:
    while True:
        user_str = input('Введите строку, если хотите прервать ввод - нажмите Enter: ')
        test_fail.writelines(f'{user_str} \n')
        if not user_str:
            break






