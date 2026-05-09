# Create a text file with student marks
file = open("students.txt", "w")
file.write("Amit 80\n")
file.write("Neha 90\n")
file.write("Rahul 70\n")
file.write("Priya 95\n")
file.write("Karan 60\n")
file.close()

# Read the file
file = open("students.txt", "r")

students = []
total = 0

for line in file:
    name, marks = line.split()
    marks = int(marks)
    students.append((name, marks))
    total += marks

file.close()

# Calculate average
avg = total / len(students)
print("Average Marks:", avg)  
# Output: Average Marks: 79.0

# Find topper
topper = students[0]
for s in students:
    if s[1] > topper[1]:
        topper = s

print("Topper:", topper)  
# Output: Topper: ('Priya', 95)

# Students below average
print("Students scoring below average:")
for s in students:
    if s[1] < avg:
        print(s)  
        # Output:
        # ('Rahul', 70)
        # ('Karan', 60)