class Student:

   def __init__(self, student):
      self.name = student['name']
      self.gender = student['gender']
      self.year = student['year']

   def get_student_details(self):
      return f"Name: {self.name}\nGender: {self.gender}\nYear: {self.year}"