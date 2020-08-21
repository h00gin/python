class ZeroExc(Exception):
    def __init__(self, txt):
        self.txt = txt


divident = input('Введите делимое: ')
dixisor = input('Введите делитель: ')

try:
    divident, dixisor = int(divident), int(dixisor)
    if dixisor == 0:
        raise ZeroExc('На ноль делить нельзя!')

except ValueError:
    print('Вы ввели не число!')

except ZeroExc as e:
    print(e)

else:
    print(f'Частное равняется: {divident / dixisor}')
