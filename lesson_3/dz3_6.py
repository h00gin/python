def intFunc(user_str):
    user_str = list(user_str)
    user_str_new = []

    for i in user_str:
        if 97 <= ord(i) <= 122:
            user_str_new.append(i)
            user_str_new1 = ''.join(user_str_new)
            user_str_new1 = user_str_new1.capitalize()
        else:
            return print('Все буквы должны быть прописными и латинскими')
    return user_str_new1


def intFuncStr(longuser_str):
    longuser_str = longuser_str.split()
    word_list = []
    for i in longuser_str:
        if type(intFunc(i)) == str:
            word_list.append(intFunc(i))
            word_str = ' '.join(word_list)
        else:
            return ('Все слова должны состоять из латинских букв')
    return word_str


print(intFuncStr('pop kljfk lkjsflkj'))
print(intFuncStr('pop 1ljfk lkjsflkj'))
# print(intFunc('ljfk333'))
# print(intFunc('ljfk'))

