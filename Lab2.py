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
        COURSE = age - 17 + 1 
        if COURSE < 1 or COURSE > 6:
            return None  
        return COURSE

    def list_name_last_name(self):
        return [self.name, self.last_name]
      
class Student(I): #дочірній класс
    def __init__(self, name=None, last_name=None, birth_year=None,
                 university=None, faculty=None, average_score=None):
        super().__init__(name, last_name, birth_year)
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

    def __indentfy_excellent(self): #приватна функція 
        if self.average_score is not None and self.average_score >= 90 #якщо більше/дорівнює 90 балів відміник
          return "Відміник"

s = Student("Богдан", "Іванюк", 2004, "ЛНУ", "Фізмат", 93)
print(s.all_information())  
print(s._Student__indentfy_excellent())
