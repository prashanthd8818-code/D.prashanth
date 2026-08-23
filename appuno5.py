# build a student record management system using
# list ,directionaries,functions , loops and condition 

students = []

def add_student():
    s = {
        "roll": input("Roll No: "),
        "name": input("Name: "),
        "marks": int(input("Marks: "))
    }
    students.append(s)
    print("Student added!")

def view_students():
    if not students:
        print("No records found")
    else:
        for s in students:
            print(s)

def search_student():
    roll = input("Enter Roll No: ")
    for s in students:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Not found")

def delete_student():
    roll = input("Enter Roll No: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Deleted!")
            return
    print("Not found")

while True:
    print("\n1.Add  2.View  3.Search  4.Delete  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program ended")
        break
    else:
        print("Invalid choice")