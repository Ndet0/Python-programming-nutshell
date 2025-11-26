# class student:
#     school = "Moringa School" #class attribute
#     def __init__(self, name, grade= 0, cohort="August 2024", unit="Biology", email=None):
#         self.name=name #instance attribute
#         self.cohort=cohort 
#         self.email=email
#         self.grade=grade
#         self.unit=unit

#         pass
    
    # def get_grade(self):
    #     return self._grade
        
    #     pass
    # def set_grade(self):
    #     if isinstance(value, (int,float) and 0 <= value <=100):
    #         self._grade = float()
    #     else:
    #         raise ValueError("Grade must be a number between 0 and 100")
    #     grade = property(get_grade, set_grade)

    #     @property
    #     def grade(self):
    #         return self._grade
    
    #     pass

    #     @grade.setter
    #     def grade(self, value):
    #         if isinstance(value, (int,float)) and 0 <= value <=100:
    #             self._grade = float(value)
    #         else:
    #             raise ValueError("Grade must be a number between 0 and 100") 



#     def greet(self):
#         print(f"Hello, my name is {self.name} from {self.cohort} cohort taking {self.unit} at {self.school}.")

#     def study(self, unit):
#         print(f"Hello I am studying {unit}")

#     pass

# alice = student("Alice")
# bob = student("Bob")

# class lecturer:

#     pass
# alice.unit="Mathematics"
# alice.cohort="June 2024"
# alice.school = "strathmore"
# print(alice.school)
# alice.greet()
# alice.study("Mathematics")
# bob.greet()

# print(type(alice))
# print(type(1))

