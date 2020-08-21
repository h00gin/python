class Date:

    # def __init__(self, str_date):
    #     self.str_date = str_date

    @classmethod
    def str_to_num(cls, str_date):
        str_date = str_date.split('-')
        number = [int(el) for el in str_date]
        return f'{number} - {Date.valid(number)}'


    @staticmethod
    def valid(number):
        for i in range(len(number)):
            if number[0] > 0 and 0 < number[1] <= 12 or 0 < number[2] <= 31:
                return ('дата задана верно')
            else:
                return ('дата задана неверно')


a = Date.str_to_num('2020-11-20')
print(a)
b = Date.str_to_num('1988-25-35')
print(b)

