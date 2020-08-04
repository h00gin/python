general_result = 0
general_result += general_result


def sumResult(user_str):
    user_str = user_str.split()
    global result, general_result
    result = 0
    for i in user_str:
        i = int(i)
        result += i
    print(f'Сумма введенных чисел равна: {result}')
    general_result += result
    print(f'Общая сумма чисел равна: {general_result}')


while True:
    user_str = input('Введите числа, разделенные прообелом, если хотите закончить расчет, нажмите "q": ')
    if user_str[-1] != 'q':
        sumResult(user_str)
    else:
        user_str = user_str[:-1]
        sumResult(user_str)
        print('Расчет закончен')
        break
