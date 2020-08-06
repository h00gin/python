from sys import argv


def wages(script_name, output, bet, prize):
    output, bet, prize = int(output), int(bet), int(prize)
    wage = (output * bet) + prize
    print(f'Заработная плата сотрудника равна: {wage}')
    print(f'Имя скрипта: {script_name}')


wages(*argv)
