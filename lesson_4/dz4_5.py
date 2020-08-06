from functools import reduce

list_random = [i for i in range (100, 1001) if i%2 == 0]

def compositionList (i, next_i):
    return i * next_i

print (reduce(compositionList, list_random))