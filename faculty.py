class Faculty:

   def __init__(self, faculty):
      self.name = faculty['name']
      self.subject = faculty['subject']

   def get_faculty_details(self):
      return f"Name: {self.name}\nSubject: {self.subject}"