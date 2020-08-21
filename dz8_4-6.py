from abc import ABC, abstractmethod


class Storage:

    def __init__(self):
        self.list_technics = []

    def to_take(self, *tec):
        for t in tec:
            self.dict_tec = {'Наименование': '', 'Количество': '', 'Цена': '', 'Характеристики': ''}
            for i in range(len(t.my_list())):
                self.dict_tec['Наименование'] = t.my_list()[0]
                self.dict_tec['Количество'] = t.my_list()[1]
                self.dict_tec['Цена'] = t.my_list()[2]
                self.dict_tec['Характеристики'] = t.my_list()[3]
            self.list_technics.append(self.dict_tec)
        return f'Список всей техники на складе:\n{self.list_technics}'

    def dict_unit(self):
        return self.list_technics

    def to_give(self, dict, *tec):  # отдает список техники
        for t in tec:
            t.take_unit(dict)


class Bookkeeping(Storage):
    def __init__(self):
        self.book_list_tec = []

    def take_unit(self, dict):  # принимает список техники в другом подразделении
        self.book_list_tec.append(dict)
        return f'Техника, находящаяся в подразделении "Бухгалтерия": {self.book_list_tec}'


class IT(Storage):
    def __init__(self):
        self.it_list_tec = []

    def take_unit(self, dict):  # принимает список техники в другом подразделении
        self.it_list_tec.append(dict)
        return f'Техника, находящаяся в подразделении "IT": {self.it_list_tec}'


class Technics(ABC):
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        Technics.valid(quantity)
        self.price = price

    @abstractmethod
    def my_list(self):
        pass

    @staticmethod
    def valid(number):  # производит валидацию количества хранимой техники
        if type(number) != int:
            print('Количество должно быть числом')


class Printer(Technics):

    def __init__(self, name, quantity, price, speed):
        super().__init__(name, quantity, price)
        self.speed = speed

    def my_list(self):
        self.info = []
        self.info.append(self.name)
        self.info.append(self.quantity)
        self.info.append(self.price)
        self.info.append(self.speed)
        return self.info


class Scanner(Technics):

    def __init__(self, name, quantity, price, resolution):
        super().__init__(name, quantity, price)
        self.resolution = resolution

    def my_list(self):
        self.info = []
        self.info.append(self.name)
        self.info.append(self.quantity)
        self.info.append(self.price)
        self.info.append(self.resolution)
        return self.info


class Xerox(Technics):

    def __init__(self, name, quantity, price, principle_scan):
        super().__init__(name, quantity, price)
        self.principle_scan = principle_scan

    def my_list(self):
        self.info = []
        self.info.append(self.name)
        self.info.append(self.quantity)
        self.info.append(self.price)
        self.info.append(self.principle_scan)
        return self.info


stor_1 = Storage()
tec_1 = Printer('Canon', 25, '35000 rub', '1500st')
tec_2 = Scanner('Epson', 30, '2500 rub', '25dpi')
tec_3 = Xerox('Xerox', 5, '30000 rub', 'ch/b')
tec_4 = Xerox('Xerox', 10, '2500 rub', 'cv')
stor_1.to_take(tec_1, tec_2, tec_3)
dict_stor_1 = stor_1.dict_unit()
print(f'Список всей техники на складе:\n {dict_stor_1}')

while True:
    name = input('Введите наименование техники, которую хотите переместить со склада (выход -  "q"): ')
    if name != 'q':
        try:
            number = int(input('Какое количество указанной техники хотите переместить: '))
            dict_stor_2 = {}  # Словарь, который передается в другое подразделение
            for i in range(len(dict_stor_1)):
                if name == dict_stor_1[i]['Наименование']:
                    dict_stor_2.update(dict_stor_1[i])
                    dict_stor_1[i]['Количество'] = dict_stor_1[i]['Количество'] - number
                # else:
                #     print('Такой техники нет на складе!')
        except ValueError:
            print('Количество должно быть числом!')
            break
        dict_stor_2.update({'Количество': number})
        subdivision = int(input('В какое подразделение хотите переметить технику ("Бухгалтерия" - 1, "IT" - 2): '))
        if subdivision == 1:
            book_1 = Bookkeeping()
            stor_1.to_give(dict_stor_2, book_1)
            print(f'Техника, находящаяся в подразделении "Бухгалтерия": {book_1.book_list_tec}')
            print(f'Остаток на складе: {dict_stor_1}')
        elif subdivision == 2:
            it_1 = IT()
            stor_1.to_give(dict_stor_2, it_1)
            print(f'Техника, находящаяся в подразделении "IT": {it_1.it_list_tec}')
            print(f'Остаток на складе: {dict_stor_1}')
        else:
            print('Такого отдела не существует')
    else:
        print('Вы вышли из программы')
        break
