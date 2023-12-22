#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
5 Создать класс Polinom для работы с многочленами до 100-й степени. Коэффициенты
должны быть представлены списоком из 100 элементов-коэффициентов. Младшая степень
имеет меньший индекс (нулевая степень — нулевой индекс). Размер списка задается как
аргумент конструктора инициализации. Реализовать арифметические операции и операции
сравнения, вычисление значения полинома для заданного значения х ,
дифференцирование, интегрирование.

Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно
храниться максимальное для данного объекта количество элементов списка; реализовать метод
size(), возвращающий установленную длину. Если количество элементов списка изменяется во
время работы, определить в классе поле count. Первоначальные значения size и count
устанавливаются конструктором.
"""

class Polinom:
    MAX_SIZE = 100

    def __init__(self, coefficients=None):
        # Проверяем, что переданный список коэффициентов имеет правильный размер
        if coefficients is None:
            coefficients = [0] * self.MAX_SIZE
        assert len(coefficients) <= self.MAX_SIZE, "Размер списка коэффициентов превышает 100"
        self.coefficients = coefficients
        self.count = len(coefficients)

    def size(self):
        # Размер списка
        return self.count

    def __repr__(self):
        # Переопределение метода для красивого вывода полинома
        terms = [f"{coef}x^{i}" if coef != 0 and i > 0 else str(coef) for i, coef in enumerate(self.coefficients)]
        return " + ".join(terms)

    def read(self):
        #Ввод с клавиатуры
        input_string = input("Введите коэффициенты полинома через пробел: ")
        coefficients = [float(coef) for coef in input_string.split()]
        return Polinom(coefficients)

    def __add__(self, other):
        # Сложение полиномов
        result_coefficients = [
            a + b for a, b in zip(self.coefficients, other.coefficients)
        ]
        return Polinom(result_coefficients)

    def __sub__(self, other):
        # Вычитание полиномов
        result_coefficients = [
            a - b for a, b in zip(self.coefficients, other.coefficients)
        ]
        return Polinom(result_coefficients)

    def __mul__(self, other):
        # Умножение полиномов
        result_coefficients = [0] * (
            len(self.coefficients) + len(other.coefficients) - 1
        )
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += (
                    self.coefficients[i] * other.coefficients[j]
                )
        return Polinom(result_coefficients)

    def __eq__(self, other):
        # Сравнение полиномов на равенство
        return self.coefficients == other.coefficients

    def evaluate(self, x):
        # Вычисление значения полинома для заданного значения x
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x**i)
        return result

    def differentiate(self):
        # Дифференцирование полинома
        result_coefficients = [i * coef for i, coef in enumerate(self.coefficients)][1:]
        return Polinom(result_coefficients)

    def integrate(self):
        # Интегрирование полинома
        result_coefficients = [
            coef / (i + 1) for i, coef in enumerate(self.coefficients)
        ]
        result_coefficients.insert(0, 0)
        return Polinom(result_coefficients)


if __name__ == "__main__":
    poly1 = Polinom([1, 2, 3])
    poly2 = Polinom().read()

    sum_poly = poly1 + poly2
    diff_poly = poly1 - poly2
    mul_poly = poly1 * poly2
    evaluated_value = poly1.evaluate(2)
    derivative_poly = poly1.differentiate()
    integral_poly = poly1.integrate()

    print("Первый полином: ", poly1)
    print("Второй полином: ", poly2)
    print("Сумма:", sum_poly)
    print("Разность:", diff_poly)
    print("Произведение:", mul_poly)
    print("Вычисление значения первого полинома при x=2:", evaluated_value)
    print("Дифференцирование первого полинома:", derivative_poly)
    print("Интегрирование первого полинома:", integral_poly)
