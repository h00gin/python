my_list = [7, 5, 3, 3, 2]
number = int(input('Введите целое число: '))
for i in range(len(my_list)):
    if number < min(my_list):
        my_list.append(number)
        break
    elif number > max(my_list):
        my_list.insert(0, number)
        break
    elif number == my_list[i]:
        my_list.insert(i + 1, number)
        break
print(my_list)
