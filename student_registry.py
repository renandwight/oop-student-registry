class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self.name = name
        self.age = age
        self.grade = grade

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        def valid_name(name):
            if len(str(name)) < 3:
                return False
            if " " in str(name):
                return False
            if not str(name).isalpha():
                return False
            if str(name).title() != str(name):
                return False
            return True
        if valid_name(new_name):
            self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        # def valid_age(age):
        #     if type(age) != 'int':
        #         return False
        #     if type(age) == 'str':
        #         return False
        #     if (type(age) is int) and (11 < age < 18):
        #         return True
        # if valid_age(new_age):
        #     self._age = new_age
        if (type(new_age) is int) and (11 < new_age < 18):
            self._age = new_age
        else:
            self._age = 13

    @property
    def grade(self):
        return self._grade
    
    @grade.setter  
    def grade(self, new_grade):
        # def valid_grade(grade):
        #     valid = ["9th", "10th", "11th", "12th"]
        #     if grade != 'str':
        #         return "12th"
        #     if grade not in valid:
        #         return "12th"
        #     return True
        valid = ["9th", "10th", "11th", "12th"]
        if new_grade in valid:
            self._grade = new_grade
        
        else:
            self._grade = "12th"

    def __str__(self):
        return (f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}.")

Student("Alice")

