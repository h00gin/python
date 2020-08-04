def degree (num_1, num_2):
    try:
        print(int(num_1) / int(num_2))
    except ZeroDivisionError:
        print('На ноль делить нельзя!')

degree('25', 5)
degree(25, 0)
degree(-32.5, 85)