from abc import ABC, abstractmethod
from math import ceil


class Dress(ABC):
    def __init__(self, size, rise):
        self.size = size
        self.rise = rise

    @abstractmethod
    def tessue_consum(self):
        raise NotImplementedError('Требуется переопределить метод!')


class Coat(Dress):
    def __init__(self, size):
        self.size = size

    @property
    def tessue_consum(self):
        # производим округление в большую сторону, так как если округлить по правилам, ткани может не хватить
        return f'Расход ткани для на производство пальто: {ceil(self.size / 6.5 + 0.5)}'


class Suit(Dress):

    def __init__(self, rise):
        self.rise = rise

    @property
    def tessue_consum(self):
        # производим округление в большую сторону, так как если округлить по правилам, ткани может не хватить
        return f'Расход ткани для на производство костюма: {ceil(2 * self.rise + 0.3)}'


# 1й способ нахождения суммарного расхода ткани:
class SumDress(Dress):

    def __init__(self, size, rise):
        super().__init__(size, rise)

    @property
    def tessue_consum(self):
        # производим округление в большую сторону, так как если округлить по правилам, ткани может не хватить
        return f'Общий расход ткани на производство одежды (1й способ): {ceil((self.size / 6.5 + 0.5) + (2 * self.rise + 0.3))}'


a = Coat(180)
print(a.tessue_consum)
b = Suit(180)
print(b.tessue_consum)
# 1й способ нахождения суммарного расхода ткани:
c = SumDress(180, 180)
print(c.tessue_consum)
# 2й способ нахождения суммарного расхода ткани:
# сумма получается больше, так как расход такани по каждому виду одежды округляется в бОльшую сторону
number_1 = ''.join(i for i in a.tessue_consum if 48 <= ord(i) <= 57)
number_2 = ''.join(j for j in b.tessue_consum if 48 <= ord(j) <= 57)
print(f'Общий расход ткани на производство одежды (2й способ): {int(number_1) + int(number_2)}')
