user_str = input('Введите строку: ')
words = (user_str).split()
count = 0
for word in words:
    if len(word) > 10:
        count += 1
        word = word[:10]
        print (f'{count}. {word}')

    else:
        count += 1
        print (f'{count}. {word}')



