# Создайте класс Frac, типичный экземпляр которого является обыкновенной дробью. Опишите методы обращения, сложения и умножения.

class Frac(object):

    # Конструктор
    def __init__(self, numerator, denominator):
        self.numerator = numerator      # Числитель
        self.denominator = denominator  # Знаменатель

    # Перевернуть дробь
    def flip_over(self):
        a = self.numerator
        self.numerator = self.denominator
        self.denominator = a

    # Сумма текущей дроби и другой
    def summ(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Frac(new_numerator, new_denominator)

    # Произведение текущей дроби и другой
    def multiplication(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return Frac(new_numerator, new_denominator)

    # Вывести на экран
    def print(self):
        print('%d\n—\n%d' % (self.numerator,self.denominator))