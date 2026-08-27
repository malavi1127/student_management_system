from student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n1. Add Student\n2. View All\n3. Update Marks\n4. Delete Student\n5. Search\n6. Exit")
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                marks = int(input("Enter marks: "))
                manager.add_student(name, marks)
            elif choice == "2":
                manager.view_all_students()
            elif choice == "3":
                sid = int(input("Enter student ID: "))
                new_marks = int(input("Enter new marks: "))
                manager.update_marks(sid, new_marks)
            elif choice == "4":
                sid = int(input("Enter student ID: "))
                manager.delete_student(sid)
            elif choice == "5":
                name = input("Enter name to search: ")
                print(manager.search_student(name))
            elif choice == "6":
                manager.close()
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    main()