class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    @property
    def name(self):
        return {self._name}
    
    @name.setter        # Name >= 3 chars no spaces or special chars; format (Firstname Lastname)
    def set_name(self, new_name):
        def valid_name(name):
            if len(name)<3:
                return False
            if " " in name:
                return False
            if not name.alpha()
                return False
            if name.title() != name:
                return False
            return True
        if valid_name(new_name):
            self._name = new_name
        else:
            raise Exception("Invalid")
        
        self._name = new_name


    @property
    def age(self):
        return {self._age}
    
    @age.setter         # Age is an int type; age > 11 and age < 18
    def set_age(self, new_age):
        if type(new_age) != 'int':
            raise Exception()
        if new_age < 11 and new_age > 18:
            raise Exception()
        else:
            self._age = new_age

    @property
    def grade(self):
        return {self._grade}
    
    @grade.setter       # Grade is 9th through 12th; value is formatted with "th"   
    def set_grade(self, new_grade):
        if new_grade != 'int':
            raise Exception()
        if new_grade < 9 and new_grade > 12:
            raise Exception()
        else:
            self._grade = str(new_grade) + "th"

    def __str__(self):
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}."
    
    #def advance(self):      # years_advanced

        #return f"{self._name} has advanced to the {self._grade} grade."
    
    def study(self, subject):

        return f"{self._name} is studying {subject}."
    
my_student = Student("Francisco", 13, "12th")