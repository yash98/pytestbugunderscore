from main_lib.school_entities.student import Student

def test_student_ben():
    student = Student("Ben", 10)
    assert student.name == "Ben"
    assert student.age == 10