from datetime import datetime

class I:
    def __init__(self, name=None, last_name=None, birth_year=None):
        self.name = name #ім'я
        self.last_name = last_name #прізвище
        self.birth_year = birth_year #рік народження 

    def indentfy_COURSE(self): #визначення курсу
        if self.birth_year is None:
            return None

        current_year = datetime.now().year #рік зараз 
        age = current_year - self.birth_year #визначення років студента
        COURSE = age - 17 + 1 
        if COURSE < 1 or COURSE > 6:
            return None  #якщо не в межах студентського віку
        return COURSE

    def list_name_last_name(self):
        return [self.name, self.last_name]

student = I("Стас", "Кравчик", 2007)
print(student.indentfy_COURSE())
print(student.list_name_last_name())
