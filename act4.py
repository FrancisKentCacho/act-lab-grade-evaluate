
def grader():
    grades = int(input("Enter your grade: "))
    if grades < 0 or grades > 100:
        print("Invalid, Enter a value between 0 and 100!")
    elif grades >= 90:
        print(grades,"= A")
    elif grades >= 80:
        print(grades,"= B")
    elif grades >= 70:
        print(grades,"= C")
    elif grades >= 60:
        print(grades,"= D")
    elif grades >= 0:
        print(grades,"= F")

grader()

while True:
    a = input("Run again?: ")
    if a == "Yes":
        grades()

    else: 
        b = print("PROGRAM DONE")
        break