class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}"