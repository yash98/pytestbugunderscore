from main_lib.school_entities.student import Student

def test_student_john():
    student = Student("John", 20)
    assert student.name == "John"
    assert student.age == 20