numbers = int(input('Введите целое положительное число: '))
max = 0
while numbers >= 1:
    maxNumber = numbers % 10
    if maxNumber > max:
        max = maxNumber
    numbers = numbers // 10
print(max)
