#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Products:
    def __init__(self, a=0, b=0):
        a = float(a)
        b = int(b)

        if a < 0 or b < 0:
            raise ValueError("Illegal value of the denominator")

        self.__first = a
        self.__second = b

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = float(value)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        value = int(value)
        if value == 0:
            raise ValueError("Illegal value of the denominator")

        self.__second = value

    # Прочитать значения first и second. Значения вводятся через пробел
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split(" ", maxsplit=1)))

        self.__first = float(parts[0])
        self.__second = int(parts[1])

        if parts[1] == 0:
            raise ValueError()

    # Привести дробь к строке.
    def __str__(self):
        return f"{self.__first * self.__second}"

    # Вычисление стоимости товара
    def __imul__(self, rhs):  # *=
        if isinstance(rhs, Products):
            a = self.first * rhs.first
            b = self.second * rhs.second
            self.__first, self.__second = a, b
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __mul__(self, rhs):  # *
        return self.__clone().__imul__(rhs)


# Возвращение структуры требуемого типа
def make_exp(first, second):
    return Products(first, second)


if __name__ == "__main__":
    r1 = Products()
    r1.read("Введите цену и количество товара (через пробел): ")
    print(f"Стоимость товара = {r1}")
