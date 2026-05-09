# Program to find students enrolled in multiple courses

# Tuples of students in different courses
course1 = ("Amit", "Neha", "Rahul", "Priya")
course2 = ("Neha", "Karan", "Priya", "Rohit")

# Convert tuples to sets
set1 = set(course1)
set2 = set(course2)

print("Course 1 Students:", set1)  
# Output: {'Amit', 'Neha', 'Rahul', 'Priya'}

print("Course 2 Students:", set2)  
# Output: {'Neha', 'Karan', 'Priya', 'Rohit'}

# Find students enrolled in multiple courses (intersection)
common_students = set1 & set2

print("Students in multiple courses:", common_students)  
# Output: {'Neha', 'Priya'}