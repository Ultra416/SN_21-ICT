from datetime import datetime

class I:
    def __init__(self, name=None, last_name=None, birth_year=None):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def indentfy_COURSE(self):
        if self.birth_year is None:
            return None

        current_year = datetime.now().year
        age = current_year - self.birth_year
        COURSE = age - 17 + 1 # Припустимо, що студент вступає до ВНЗ у 17 років
        if COURSE < 1 or COURSE > 6:
            return None  # Якщо не в межах типового студентського віку
        return COURSE

    def list_name_last_name(self):
        return [self.name, self.last_name]
      
class Student(I):
    def __init__(self, name=None, last_name=None, birth_year=None,
                 university=None, факультет=None, середній_бал=None):
        super().__init__(ім'я, прізвище, рік_народження)
        self.university = university
        self.faculty = faculty
        self.average_score = average_score

    def all_information(self):
        return {
            "ПІБ": f"{self.name} {self.last_name}",
            "Рік народження": self.birth_year,
            "Університет": self.university,
            "Факультет": self.faculty,
            "Середній бал": self.average_score,
            "Курс": self.indentfy_COURSE()
        }

    def __indentfy_score(self):
        return self.average_score is not None and self.average_score >= 90

s = Student("Богдан", "Іванюк", 2004, "ЛНУ", "Фізмат", 93)
print(s.all_information())  # Не спрацює напряму — бо метод приватний
print(s._Student__indentfy_score())  # Доступ до приватного методу (Python-механіка)
