class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students

# Example usage:
students = [
  Student("Nishanth", "A101", 7.4),
  Student("Nitheesh", "A102", 8.6),
  Student("Shamini", "A103", 9.8),
  Student("Akilesh", "A104", 9.2),
]

sorted_students = sort_students(students)

# Print the sorted students
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
