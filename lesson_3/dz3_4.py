# 1е решение
def exponentiation1(x, y):
    if type(x) == int and x >= 0 and type(y) == int and y < 0:
        return x ** y
    else:
        return print('Введите действительное положительное число x  и целое отрицательное число y')

# 2е решение
def exponentiation2(x, y):
    if type(x) == int and x >= 0 and type(y) == int and y < 0:
        result = 1
        for i in range (abs(y)):
            result *= 1/x
        return result
    else:
        return ('Введите действительное положительное число x  и целое отрицательное число y')
print(exponentiation2(2, -4))
print(exponentiation2(3, 3))
