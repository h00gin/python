class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.complex_num = complex(a, b)


    def __add__(self, other):
        return f'Сумма комплексных чисел равна: {complex((self.a + other.a), (self.b + other.b))}'

    def __mul__(self, other):
        return f'Произведение комплексных чисел равно:' \
               f'{complex((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))}'


num_1 = ComplexNum(2, 5)
print(f'Первое комплексное число: {num_1.complex_num}')

num_2 = ComplexNum(6, 8)
print(f'Второе комплексное число равно: {num_2.complex_num}')
print(num_1 + num_2)
print(num_1 * num_2)
