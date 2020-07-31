lenght = int(input('Введите длину списка: '))
elements = []
for i in range(lenght): #заполенение списка элементами. элементы вводит пользователь
    element = input(f'Введите {i+1}й элемент списка: ')
    elements.append(element)
print(elements)

for i in range(0, len(elements)-1, 2): #меняем местами соседние элементы списка
    elements[i], elements[i+1] = elements[i+1], elements[i]
print(elements)
