class ListNum(Exception):
    def __init__(self, txt):
        self.txt = txt


list_num = []
while True:
    el = input('Введите элемент списка: ')

    try:
        if el == 'q':
            break
        if not el.isdigit():
            raise ListNum('В списке должны быть только цифры')

    except ListNum as e:
        print(e)

    else:
        el = int(el)
        list_num.append(el)

print(list_num)