# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Введите число: "))

if num <= 1 or num > 100000:
    print("Число должно быть больше 1 и меньше 100000")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "является простым числом")
    else:
        print(num, "является составным числом")