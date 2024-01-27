import pytest
from student import Student


def test_student():
    student = Student("Иван Иванов", "subjects.csv")
    assert student.name == "Иван Иванов"


def test_add_grade():
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    assert student.subjects["Математика"]["grades"] == [4]


# Тесты
def test_invalid_data(caplog):
    with pytest.raises(ValueError):
        # Student("Иванов Иван Иванович", "wrong_file.csv")
        Student("Иванов Иван Иванович", "subjects.csv")
    assert 'Не удалось загрузить предметы' in caplog.text


def test_add_grade_existing_subject(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    student.add_grade("Математика", 4)
    assert student.subjects["Математика"]["grades"] == [4]
    assert 'Добавляю оценку 4 для предмета Математика для студента Иванов Иван Иванович' in caplog.text


def test_add_test_score(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    student.add_test_score("Математика", 85)
    assert student.subjects["Математика"]["test_scores"] == [85]
    assert 'Добавляю результат теста 85 для предмета Математика для студента Иванов Иван Иванович' in caplog.text


def test_calculate_average_grade(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    assert student.get_average_grade("Математика") == 4.5
    assert 'Вычисляю средний балл для студента Иванов Иван Иванович' in caplog.text


def test_calculate_average_test_score(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    student.add_test_score("Математика", 85)
    student.add_test_score("Математика", 90)
    assert student.get_average_test_score("Математика") == 87.5
    assert 'Вычисляю средний результат теста для предмета Математика для студента Иванов Иван Иванович' in caplog.text


def test_get_average_grade_nonexistent_subject(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    with pytest.raises(ValueError):
        student.get_average_grade("Физика")
    assert 'Предмет Физика не найден' in caplog.text


def test_get_average_test_score_nonexistent_subject(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    with pytest.raises(ValueError):
        student.get_average_test_score("Физика")
    assert 'Предмет Физика не найден' in caplog.text


def test_add_grade_nonexistent_subject(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    with pytest.raises(AttributeError):
        student.add_grade("Физика", 5)
    assert 'Предмет Физика не найден' in caplog.text


def test_add_test_score_nonexistent_subject(caplog):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    with pytest.raises(AttributeError):
        student.add_test_score("Физика", 90)
    assert 'Предмет Физика не найден' in caplog.text


@pytest.mark.parametrize(
    "subject, grade",
    [
        ("Математика", 4),
        ("История", 5),
    ]
)
def test_add_grade_parameterized(subject, grade):
    student = Student("Иванов Иван Иванович", "subjects.csv")
    student.add_grade(subject, grade)
    assert student.subjects[subject]["grades"] == [grade]
