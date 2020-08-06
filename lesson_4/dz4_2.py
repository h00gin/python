import random

my_list = [random.randint(0, 1000) for i in range(0, 10)]

list_new = [my_list[i + 1] for i in range(len(my_list) - 1) if my_list[i + 1] > my_list[i]]
print(my_list)
print(list_new)
