students_grade=[]
students_grade.append((2,"Ankitha"))
students_grade.append((1,"Rishi"))
students_grade.sort(reverse=True)
print("yes")
print(students_grade)
students_grade.append((4,"Teju"))
students_grade.sort(reverse=True)
students_grade.append((3,"Yochana"))
students_grade.sort(reverse=True)
print("priority wise")
print(students_grade)
print("original queue")
while students_grade:
    print(students_grade.pop())