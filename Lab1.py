from datetime import datetime

class I:
    def __init__(self, name=None, last_name=None, birth_year=None):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year

    def Indentfy_COURSE(self):
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
