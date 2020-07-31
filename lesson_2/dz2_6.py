products = [] #список введенных словарей без нумерации
number = int(input('Введите количество наименований товаров, которое хотиле внести в базу: '))

for i in range(number):
    my_dict = {'название': '', 'цена': '', 'количество': '', 'ед.': 'шт.'}
    my_dict['название'] = input('Введите наименование товара: ')
    my_dict['цена'] = int(input('Введите цену товара: '))
    my_dict['количество'] = int(input('Введите количество товара: '))
    my_dict['ед.'] = input('Введите единицу учета товара: ')
    products.append(my_dict)

products_number = [] #список кортежей нумерация + введенные словари с нумерацией
for j in enumerate(products, 1):
    products_number.append(j)
print(products_number)

#сортировка получившегося списка товаров (аналитика)
name = []
price = []
quantity = []
unit = []
for i in range(len(products_number)):
    name.append(products_number[i][1].get('название'))
    price.append(products_number[i][1].get('цена'))
    quantity.append(products_number[i][1].get('количество'))
    unit.append(products_number[i][1].get('ед.'))
analitics = {'название': name, 'цена': price, 'количество': quantity, 'ед.': unit}
print(analitics)
