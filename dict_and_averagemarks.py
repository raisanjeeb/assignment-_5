
# Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

# Use a loop to print each student's name and mark
for name, mark in students.items():
    print(name, ":", mark)

# Calculate average mark
total = sum(students.values())
average = total / len(students)

print("Average mark of all students:", average)
