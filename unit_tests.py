import pytest
from app import init_db, add_or_update_course, view_courses, deleteAll_course, \
    add_or_update_student, view_students, deleteAll_students

@pytest.fixture(autouse=True)
def setup_and_teardown():
    init_db()
    deleteAll_students()
    deleteAll_course()
    # add_or_update_course("Existing Course 1", "Description 1")
    # add_or_update_course("Existing Course 2", "Description 2")
    # add_or_update_student("Existing Student 1", "test1@example.com", "123456789", 1)
    # add_or_update_student("Existing Student 2", "test2@example.com", "987654321", 2)
    yield

def test_add_and_view_course():
    add_or_update_course("Test Course", "Test Description")
    courses = view_courses()
    assert len(courses) == 1

def test_delete_course():
    courses_before_deletion = view_courses()
    deleteAll_course()
    courses_after_deletion = view_courses()
    assert len(courses_after_deletion) == 0

def test_add_and_view_student():
    add_or_update_student("New Student", "newstudent@example.com", "555555555", 2)
    students = view_students()
    assert len(students) == 1

def test_delete_student():
    students_before_deletion = view_students()
    deleteAll_students()
    students_after_deletion = view_students()
    assert len(students_after_deletion) == 0
