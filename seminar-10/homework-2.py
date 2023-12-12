# Создание двух списков чисел
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# Определение класса LotteryGame


class LotteryGame:

    # Инициализация объекта класса с двумя списками
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    # Метод для сравнения двух списков и нахождения совпадающих чисел
    def compare_lists(self):
        # Создание пустого списка для совпадающих чисел
        matching_numbers = []

        # Перебор всех чисел в первом списке
        for num1 in self.list1:
            # Если число присутствует во втором списке, добавить его в список совпадающих чисел
            if num1 in self.list2:
                matching_numbers.append(num1)

        # Если список совпадающих чисел не пуст, вывести эти числа и их количество
        if matching_numbers:
            print("Совпадающие числа:", matching_numbers)
            print("Количество совпадающих чисел:", len(matching_numbers))
        # Если список совпадающих чисел пуст, вывести сообщение об отсутствии совпадений
        else:
            print("Совпадающих чисел нет.")

        # Возвращение списка совпадающих чисел
        return matching_numbers


# Создание объекта класса LotteryGame с двумя списками чисел
game = LotteryGame(list1, list2)
# Вызов метода compare_lists для нахождения и вывода совпадающих чисел
matching_numbers = game.compare_lists()
