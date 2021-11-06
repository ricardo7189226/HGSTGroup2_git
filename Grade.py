print("\n\n\n       Grade Calculator for multiple Students")
print("----------------------------------------------------")
count = int(input("Enter the Number of Students : "))

for i in range(count):
    print("\n----------------------------------------------------")
    StudentName = input("Enter Student Name : ")
    Prelims = int(input("Enter Prelim Average Grade:\t "))
    Midterm = int(input("Enter Midterm Average Grade:\t "))
    Semifinal = int(input("Enter SemiFinal Average Grade:\t "))
    Final = int(input("Enter Final Average Grade:\t "))
    Average = (Prelims + Midterm + Semifinal + Final)/4

    print("\nAverage Grade:\t", Average)