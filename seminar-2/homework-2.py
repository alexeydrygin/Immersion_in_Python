# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

# from decimal import Decimal
# from fractions import Fraction


# def read_value(number_val: int) -> list:
#     """
#     Функция возвращает введенные переменные в формате list
#     :param number_val: номер вводимых переменных
#     :return: переменные в формате list
#     """
#     while True:
#         str_val = input(f'Введите строку {number_val} в формате a/b: ')
#         list_val = str_val.split('/')
#         if len(list_val) == 2 and list_val[0].isdigit() and list_val[1].isdigit():
#             list_val.append(str_val)
#             return list_val
#         else:
#             print('Не верный формат. Введите числа в формате a/b')


# val_1 = read_value(1)
# val_2 = read_value(2)

# frac1 = "4/8"
# frac2 = "1/2"

# print(f'Сумма дробей:                 {Decimal(val_1[0]) / Decimal(val_1[1]) + Decimal(val_2[0]) / Decimal(val_2[1])}')
# print(f'Проверка суммы дробей:        {Fraction(val_1[2]) + Fraction(val_2[2])}')
# print()
# print(f'Произведение дробей:          {Decimal(val_1[0]) / Decimal(val_1[1]) * Decimal(val_2[0]) / Decimal(val_2[1])}')
# print(f'Проверка произведения дробей: {Fraction(val_1[2]) * Fraction(val_2[2])}')










from fractions import Fraction

frac1 = "2/3"
frac2 = "3/4"
# Разбиваем строки на числитель и знаменатель без использования map
numerator1_str, denominator1_str = frac1.split('/')
numerator2_str, denominator2_str = frac2.split('/')
# 
# # Преобразуем строки в целые числа
numerator1 = int(numerator1_str)
denominator1 = int(denominator1_str)
numerator2 = int(numerator2_str)
denominator2 = int(denominator2_str)

common_denominator = denominator1 * denominator2

new_numerator1 = numerator1 * denominator2
new_numerator2 = numerator2 * denominator1

summation_numerator = new_numerator1 + new_numerator2
multiplication_numerator = numerator1 * numerator2

print(f"Сумма дробей: {summation_numerator}/{common_denominator}")
print(f"Произведение дробей: {multiplication_numerator}/{common_denominator}")

# Преобразуем введенные строки в объекты Fraction
fraction1 = Fraction(frac1)
fraction2 = Fraction(frac2)

# Вычисляем сумму и произведение дробей
summation = fraction1 + fraction2
multiplication = fraction1 * fraction2

print(f"Сумма дробей: {summation}")
print(f"Произведение дробей: {multiplication}")
