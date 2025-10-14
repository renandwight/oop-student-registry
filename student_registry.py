class Student:
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    def name(self):
        
        return {self._name}
    
    @name.setter        # Name >= 3 chars no spaces or special chars; Title format

    def age(self):
        
        return {self._age}
    
    @age.setter         # Age is an int type; age > 11 and age < 18

    def grade(self):
        
        return {self._grade}
    
    @grade.setter       # Grade is 9th through 12th; value is formatted with "th"   
    
    def __str__(self):
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {grade}th."
    
    def advance(self):      # years_advanced

        return f"{self.name} has advanced to the {grade}th grade."
    
    def study(self, subject):

        return f"{self.name} is studying {subject}"
    
my_student = Student("Francisco", 13, "12th")