def fact (n):
    numbers = [i for i in range(1, n+1)]
    fact = 1
    for i in range(len(numbers)):
        fact = fact * numbers[i]
        yield fact

for el in fact(4):
    print(el)


#