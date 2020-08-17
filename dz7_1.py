class Matrix:

    def __init__(self, matrix):
        try:
            self.user_list =  matrix

        except TypeError:
            print('Вводимые данные должны быть списком!')

    def __add__(self, other):
        result_list_2 = []
        for i, j in zip(range(len(self.user_list)), range(len(other.user_list))):
            result_list_1 = [x + y for x, y in zip(self.user_list[i], other.user_list[j])]
            result_list_2.append(result_list_1)
        return Matrix(result_list_2)

    def __str__(self):
        self.user_str_sum = ''
        for i in range(len(self.user_list)):
            # user_str = ''.join((user_str + '\t' + str(el) + ' ') for el in self.user_list[i] if el != ',')
            user_str = ''
            for el in self.user_list[i]:
                if el != ',' and ' ':
                    user_str = user_str + '\t' + str(el) + '\t'
            self.user_str_sum = self.user_str_sum + user_str + '\n'
        return f'Матрица в привычном виде:\n{self.user_str_sum}'


a = Matrix([[25, 25, 55], [25, 25, 55], [28, 68, 98]])
b = Matrix([[85, 100, 222], [25, 65, 121], [55, 87, 45]])

print(a)
print(b)
print(a + b)
