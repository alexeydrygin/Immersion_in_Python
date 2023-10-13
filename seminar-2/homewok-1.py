num = 0


# def int_to_hex(num):
#     return hex(num)[2:]

# def int_to_hex_format(num):
#     if num == 0: # костыль, который вместо нуля выдает пробел
#         return ''
#     else:
#         return format(num, 'X')


# hex_num = int_to_hex(num)
# hex_num_format = int_to_hex_format(num)

# print(f"Шестнадцатеричное представление числа: {hex_num_format}")
# print(f"Проверка результата: 0x{hex_num}")

################ РЕШЕНИЕ ОТ GB "ЭТАЛОННОЕ!!!" ####################

HEX = 16
hex_digits = "0123456789ABCDEF"

hex_num = ""
test_hex_num = hex(num)

while num > 0:
    remainder = num % HEX
    hex_num = hex_digits[remainder] + hex_num
    num //= HEX

print("Шестнадцатеричное представление числа:", hex_num)
print("Проверка результата:", test_hex_num)