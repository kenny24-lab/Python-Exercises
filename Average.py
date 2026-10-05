students = []
marks = []

for i in range(3):

    name = input("Student name: ")
    mark = float(input("Mark: "))

    students.append(name)
    marks.append(mark)

average = sum(marks) / len(marks)

print("Average:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))