def userDate (name, surname, year, city, email, telephone):
    print(f'{name} {surname}; '
          f'год рождения: {year}; '
          f'город проживания: {city}; '
          f'адрес электронной почты: {email}; '
          f'номер телефона: {telephone}.')

userDate(name='Виктор',
         surname='Рогов',
         year=1986, city='Волгоград',
         email='h00gin@yandex.ru',
         telephone=89176481797)