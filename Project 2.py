for i in range(1,6): # stuent name
    print("Enter the Student Name", i)
    studentname = input()
    totalmarks = 0
    for j in range(1,6): # marks
        print(studentname,"subject",j)
        subjectmarks = float(input())
        totalmarks += subjectmarks
    print("Total mark for",studentname,"is :",totalmarks)
    print("=================================================")