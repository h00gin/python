user_second = int(input('Введите время в секундах: '))
hours = user_second//3600
minutes = (user_second - 3600*hours)//60
seconds = user_second - 3600*hours - 60*minutes

print (f'Время: {hours:02}:{minutes:02}:{seconds:02}')