from database import (create_student,
                                      delete_student,
                                      view_all_students,
                                      view_student_by_department,
                                      view_students_by_semester,
                                      update_student_semester_db,
                                      view_students_by_department_and_semester,
                                      view_student_by_id
                                      )
import exceptions

def add_student(name,department,semester):
    if semester<1 or semester>8:
        raise exceptions.ValidationError("Semester must be between 1 and 8.")
    else:
        return create_student(name,department,semester)

def get_all_students():
    x=view_all_students()
    if not x:
        raise exceptions.ResourceNotFoundError("No students found.")
    return x

def get_students_by_department(department):

    x=view_student_by_department(department)
    if not x:
        raise exceptions.ResourceNotFoundError("No students found in this department.")
    return x

def get_students_by_semester(semester):

    x=view_students_by_semester(semester)
    if not x:
        raise exceptions.ResourceNotFoundError("No students found in this semester.")
    return x

def get_students_by_department_and_semester(department=None,semester=None):
    x=view_students_by_department_and_semester(department,semester)
    if not x:
        raise exceptions.ResourceNotFoundError("No students found in this department and semester.")
    return x

def get_student_by_id(student_id):
    x=view_student_by_id(student_id)
    if not x:
        raise exceptions.ResourceNotFoundError("Student not found.")
    return x

def update_student(semester,student_id):
    if semester < 1 or semester > 8:
        raise exceptions.ValidationError("Semester must be between 1 and 8.")
    temp=get_student_by_id(student_id)
    if temp:
        x=update_student_semester_db(semester,student_id)
    return x

def remove_student(student_id):
    x=delete_student(student_id)
    if not x:
        raise exceptions.ResourceNotFoundError("Student not found.")
    return x