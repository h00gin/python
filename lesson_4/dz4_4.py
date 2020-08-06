my_list = [input(f'Введите {i+1}й элемент списка: ') for i in range(5)]

new_list = [i for i in my_list if my_list.count(i) == 1]

print(my_list)
print(new_list)
