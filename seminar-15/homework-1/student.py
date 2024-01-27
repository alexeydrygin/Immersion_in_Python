import csv
import logging
import os



# Настройка логирования
# logging.basicConfig(filename='seminar-15/app_student.log', encoding='utf-8',
#                     level=logging.DEBUG, format='%(asctime)s - %(message)s')
logging.basicConfig(filename='seminar-15/app_student.log', encoding='utf-8',
                    level=logging.DEBUG)


class Student:
    """
    Класс, представляющий студента.

    Атрибуты:
    - name (str): ФИО студента
    - subjects (dict): словарь, содержащий предметы и их оценки и результаты тестов

    Методы:
    - __init__(self, name, subjects_file): конструктор класса
    - __setattr__(self, name, value): дескриптор, проверяющий ФИО на первую заглавную букву и наличие только букв
    - __getattr__(self, name): получение значения атрибута
    - __str__(self): возвращает строковое представление студента
    - load_subjects(self, subjects_file): загрузка предметов из файла CSV
    - get_average_test_score(self, subject): возвращает средний балл по тестам для заданного предмета
    - get_average_grade(self): возвращает средний балл по всем предметам
    - add_grade(self, subject, grade): добавление оценки по предмету
    - add_test_score(self, subject, test_score): добавление результата теста по предмету
    """

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        absolute_path = os.path.abspath(subjects_file)
        if not os.path.exists(absolute_path):
            raise ValueError("Не удалось загрузить предметы")
        self.load_subjects(absolute_path)

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                raise ValueError(
                    "ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        try:
            logging.info(
                f"Загружаю предметы из файла {subjects_file} для студента {self.name}")
            with open(subjects_file, encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    subject = row[0]
                    if subject not in self.subjects:
                        self.subjects[subject] = {
                            'grades': [], 'test_scores': []}
        except Exception as e:
            logging.exception("Не удалось загрузить предметы")

    def add_grade(self, subject, grade):
        try:
            logging.info(
                f"Добавляю оценку {grade} для предмета {subject} для студента {self.name}")
            if subject not in self.subjects:
                self.subjects[subject] = {'grades': [], 'test_scores': []}
            if not isinstance(grade, int) or grade < 2 or grade > 5:
                raise AttributeError("Оценка должна быть целым числом от 2 до 5")
            self.subjects[subject]['grades'].append(grade)
        except Exception as e:
            logging.exception("Не удалось добавить оценку")

    def add_test_score(self, subject, test_score):
        try:
            logging.info(
                f"Добавляю результат теста {test_score} для предмета {subject} для студента {self.name}")
            if subject not in self.subjects:
                self.subjects[subject] = {'grades': [], 'test_scores': []}
            if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
                raise AttributeError(
                    "Результат теста должен быть целым числом от 0 до 100")
            self.subjects[subject]['test_scores'].append(test_score)
        except Exception as e:
            logging.exception("Не удалось добавить результат теста")

    def get_average_test_score(self, subject):
        try:
            logging.info(
                f"Вычисляю средний результат теста для предмета {subject} для студента {self.name}")
            if subject not in self.subjects:
                raise ValueError(f"Предмет {subject} не найден")
            test_scores = self.subjects[subject]['test_scores']
            if len(test_scores) == 0:
                return 0
            return sum(test_scores) / len(test_scores)
        except Exception as e:
            logging.exception("Не удалось вычислить средний результат теста")

    def get_average_grade(self):
        try:
            logging.info(f"Вычисляю средний балл для студента {self.name}")
            total_grades = []
            for subject in self.subjects:
                grades = self.subjects[subject]['grades']
                if len(grades) > 0:
                    total_grades.extend(grades)
            if len(total_grades) == 0:
                return 0
            return sum(total_grades) / len(total_grades)
        except Exception as e:
            logging.exception("Не удалось вычислить средний балл")

student = Student("Иванов Иван Иванович", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)

