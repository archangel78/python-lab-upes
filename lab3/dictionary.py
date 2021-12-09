student_dictionary = {}
no_students = int(input("Enter number of students: "))
no_subjects = int(input("Enter number of subjects: "))

for i in range(1,no_students+1):
    print("")
    student_name = input("Enter student "+str(i)+" name: ")
    student_dictionary[student_name] = []
    for j in range(1,no_subjects+1):
        print("Enter student "+str(i)+" subject "+str(j)+" marks: ",end="")
        student_marks = float(input())
        student_dictionary[student_name].append(student_marks)

print("***********************************************************************************\nAverage marks: ")

for student in student_dictionary:
    total_marks = 0
    for mark in range(0,no_subjects):
        total_marks = total_marks + student_dictionary[student][mark]

    average_marks = total_marks/no_subjects
    print(student+": "+str(average_marks))