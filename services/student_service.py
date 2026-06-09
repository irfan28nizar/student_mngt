from database import (create_student,
                                      delete_student,
                                      view_all_students,
                                      view_student_by_department,
                                      view_students_by_semester,
                                      update_student_semester_db,
                                      view_students_by_department_and_semester,
                                      view_student_by_id
                                      )

def add_student(name,department,semester):
    if semester<1 or semester>8:
        raise ValueError("Semester must be between 1 and 8.")
    else:
        return create_student(name,department,semester)
def get_all_students():
    return view_all_students()
def get_students_by_department(department):
    return view_student_by_department(department)
def get_students_by_semester(semester):
    return view_students_by_semester(semester)
def get_students_by_department_and_semester(department=None,semester=None):
    return view_students_by_department_and_semester(department,semester)
def get_student_by_id(student_id):
    return view_student_by_id(student_id)
def update_student(student_id,semester):
    if semester < 1 or semester > 8:
        raise ValueError("Semester must be between 1 and 8.")
    return update_student_semester_db(semester,student_id)
def remove_student(student_id):
    return delete_student(student_id)