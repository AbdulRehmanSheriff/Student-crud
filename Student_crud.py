# student_crud.py

students = {}

def create_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    students[roll] = name
    print(f"Student {name} added!")

def read_students():
    if not students:
        print("No records found.")
    else:
        print("\nStudent Records:")
        for roll, name in students.items():
            print(f"Roll: {roll}, Name: {name}")

def update_student():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        students[roll] = name
        print("Record updated successfully!")
    else:
        print("Record not found!")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Record deleted!")
    else:
        print("Record not found!")

def menu():
    while True:
        print("\n--- Student CRUD Application ---")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            create_student()
        elif choice == "2":
            read_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
