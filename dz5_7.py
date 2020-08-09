import json

with open('text_7.txt', 'r', encoding='utf-8') as list_firm, open('text_7j.json', 'w', encoding='utf-8') as new_file:
    profit_list = [] #общий список, включая словарь фирм и среднюю прибыль
    profit_dict = {} #словарь с названием фирмы и прибылью
    average_profit = 0 #средняя прибыль
    firm_plus = 0 #количество фирм с прибылью
    sum_profit = 0 #суммарная прибыль фирм
    for line in list_firm:
        line = line.split()
        for i in range(len(line)):
            profit = int(line[2]) - int(line[3])
        if profit > 0:
            firm_plus += 1
            sum_profit += profit
        profit_dict.update({line[0]: profit})
    profit_list.append(profit_dict)
    average_profit = sum_profit/firm_plus
    profit_list.append({'average_profit': average_profit})
    json.dump(profit_list, new_file,indent= 4, ensure_ascii= False)

