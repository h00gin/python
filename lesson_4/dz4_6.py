from itertools import count,cycle

for i in count(3):
    if i > 10:
        break
    else:
        print(i)

counter = 0
user_list = [input(f'Введите {i+1}й элемент списка, состоящий из 3 слов: ') for i in range(3)]
print(user_list)
for element in cycle(user_list):
    if counter > 5:
        break
    print(element)
    counter+=1

