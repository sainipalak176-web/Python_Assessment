# Grading System Program

# Input marks of 5 subjects
s1 = float(input("Enter marks of Subject 1: "))   # 80
s2 = float(input("Enter marks of Subject 2: "))   # 85
s3 = float(input("Enter marks of Subject 3: "))   # 90
s4 = float(input("Enter marks of Subject 4: "))   # 88
s5 = float(input("Enter marks of Subject 5: "))   # 92

# Calculate total and percentage
total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

# Display percentage
print("Percentage:", percentage)   # Output: Percentage: 87.0

# Assign grade using nested if-else
if percentage >= 90:
    grade = "A+"
else:
    if percentage >= 75:
        grade = "A"
    else:
        if percentage >= 60:
            grade = "B"
        else:
            if percentage >= 50:
                grade = "C"
            else:
                grade = "Fail"

print("Grade:", grade)   # Output: Grade: A

# Scholarship condition
# (Scholarship if percentage >= 85 and all subjects >= 60)

if percentage >= 85:
    if s1 >= 60 and s2 >= 60 and s3 >= 60 and s4 >= 60 and s5 >= 60:
        print("Scholarship: Eligible")  
        # Output: Scholarship: Eligible
    else:
        print("Scholarship: Not Eligible (Low marks in one or more subjects)")
else:
    print("Scholarship: Not Eligible (Percentage less than 85)")