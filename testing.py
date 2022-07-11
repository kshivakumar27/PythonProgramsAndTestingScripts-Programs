# importing the Student and Faculty classes from respective files
from student import Student
from faculty import Faculty

# creating dicts for student and faculty
student_dict = {'name' : 'John', 'gender': 'Male', 'year': '3'}
faculty_dict = {'name': 'Emma', 'subject': 'Programming'}

# creating instances of the Student and Faculty classes
student = Student(student_dict)
faculty = Faculty(faculty_dict)

# getting and printing the student and faculty details
print(student.get_student_details())
print()
print(faculty.get_faculty_details())