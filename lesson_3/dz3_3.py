def funcSum(num_1, num_2, num_3):
    try:
        result = [num_1, num_2, num_3]
        max_number_1 = max(result)
        for num in result:
            if num == max_number_1:
                result.remove(num)
        max_number_2 = max(result)
        return (max_number_1 + max_number_2)
    except TypeError:
        return ('Все значения должны быть числами!')

print(funcSum(25, 86, -85))
print(funcSum('25', 385, -8888))