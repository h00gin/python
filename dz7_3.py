class Cell:

    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return f'Сумма равна: {self.nucleus + other.nucleus}'

    def __sub__(self, other):
        if (self.nucleus - other.nucleus) > 0:
            return f'Разность равна: {self.nucleus - other.nucleus}'
        else:
            return 'Разность меньше 0!'

    def __mul__(self, other):
        return f'Произведение равно: {self.nucleus * other.nucleus}'

    def __floordiv__(self, other):
        return f'Целочисленное деление равно: {self.nucleus // other.nucleus}'

    def make_order(self, pow):
        result_1 = ''.join('*' for i in range(self.nucleus))
        result_2 = '\n'.join(result_1[i:i+pow] for i in range(0, len(result_1), pow))

        return f'Органическая клетка, состоящая из {self.nucleus} ячеек,' \
               f' с количеством ячеек в ряду равным {pow}:\n{result_2}'

a = Cell(15)
b = Cell(5)
c = Cell(27)
print(a.make_order(5))
print(b.make_order(5))
print(c.make_order(6))

print(a+b)
print(a-b)
print(b-a)
print(a*b)
print(a//b)



