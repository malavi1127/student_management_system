import importlib

try:
    mysql_connector = importlib.import_module("mysql.connector")
except ImportError as exc:
    raise ImportError(
        "mysql-connector-python is required. Install it with "
        "'pip install mysql-connector-python'."
    ) from exc

class StudentManager:
    def __init__(self):
        self.conn = mysql_connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="student_database"
        )
        self.cursor = self.conn.cursor()

    def add_student(self, name, marks):
        self.cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", (name, marks))
        self.conn.commit()
        print(f"Student {name} added successfully")

    def view_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        for row in self.cursor.fetchall():
            print(row)

    def update_marks(self, student_id, new_marks):
        self.cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (new_marks, student_id))
        self.conn.commit()
        print("Marks updated successfully")

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        self.conn.commit()
        print("Student deleted successfully")

    def search_student(self, name):
        self.cursor.execute("SELECT * FROM students WHERE name = %s", (name,))
        result = self.cursor.fetchall()
        return result if result else "Student not found"

    def close(self):
        self.conn.close()