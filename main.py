import json


data_file = "db.json"


def read_db_data():
    """Read student data from JSON file.

    Returns an empty list when the file does not exist or contains
    invalid JSON (e.g. empty file). This prevents json.load from
    raising a JSONDecodeError when `db.json` exists but is empty.
    """
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        # No DB file yet — start with empty list
        return []
    except json.JSONDecodeError:
        # File exists but is empty or contains invalid JSON
        print("Warning: db.json is empty or contains invalid JSON — starting with empty list.")
        return []


def save_db_data(students):
    """Save student data to JSON file."""
    try:
        with open(data_file, "w") as file:
            json.dump(students, file, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")


def add_new_student():
    """Prompt user to add a new student to the database."""
    students = read_db_data()
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    student_id = input("Enter student ID: ")

    new_student = {
        "name": name,
        "age": age,
        "id": student_id
    }

    students.append(new_student)
    save_db_data(students)
    print("Student added successfully!")


def view_students():
    """Display all students."""
    students = read_db_data()
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")


def main():
    """Main menu loop."""
    while True:
        print("\n--- Student Management System ---")
        print("1. Add new student")
        print("2. View students")
        print("3. Edit student")
        print("4. Delete student")
        print("5. Exit")

        option = input("Enter your choice (1-5): ")

        if option == "1":
            add_new_student()
        elif option == "2":
            view_students()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
    