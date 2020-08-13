class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {}
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'Данные сотрудника: \nИмя: {self.name}, Фамилия: {self.surname}\n')

    def get_total_income(self):
        print(f'Доход сотрудника с учетом премии: {self.wage + self.bonus}\n')


a = Position('Василий', 'Пупкин', 'уборщик', 20000, 5000)
a.get_full_name()
a.get_total_income()
b = Worker('Виктор', 'Скворцов', 'автоэксперт', 50000, 25000)
print(b._Worker__income)

