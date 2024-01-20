import re
import sys
import doctest

class NegativeValueError(ValueError):
    pass

class Rectangle:

    def __init__(self, width, height=None):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.width
        5
        >>> r1.height
        5
        >>> r2 = Rectangle(3, 4)
        >>> r2.width
        3
        >>> r2.height
        4
        >>> r3 = Rectangle(-2)
        Traceback (most recent call last):
        ...
        NegativeValueError: Ширина должна быть положительной, а не -2
        >>> r4 = Rectangle(5, -3)
        Traceback (most recent call last):
        ...
        NegativeValueError: Высота должна быть положительной, а не -3
        '''
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')

    def perimeter(self):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        '''
        return 2 * (self._width + self._height)

    def area(self):
        '''
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        '''
        return self._width * self._height

    def __add__(self, other):
        '''
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        '''
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        '''
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        '''
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)
    
######################################################################################################################
    
# Открываем файл для записи
with open('pytest_output.txt', 'w') as file:
    # Перенаправляем stdout в файл
    sys.stdout = file

    # Запускаем pytest.main() с нужными параметрами
    __file__ = None

    doctest.testmod(extraglobs={'__file__': __file__})

# Возвращаем stdout в исходное состояние
sys.stdout = sys.__stdout__
# Считываем содержимое файла
with open('pytest_output.txt', 'r') as file:
    lines = file.readlines()
    # first_line = file.readline()
    # first_five_lines = lines[:1]


file_name = "pytest_output.txt.txt"

# Открываем файл на чтение
with open('pytest_output.txt', "r") as file:
    # Считываем содержимое файла
    file_content = file.read()

# Используем регулярное выражение для удаления "line" и чисел после него
cleaned_content = re.sub(r'File "__main__", line \d+', '', file_content)

# Записываем обновленное содержимое обратно в файл
with open(file_name, "w") as file:
    file.write(cleaned_content)

with open(file_name, 'r') as new_file:
    file_contents = new_file.read()
    # Выводим содержимое файла на экран
    print(file_contents)
