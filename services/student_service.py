from database import (create_student,
                                      delete_student,
                                      update_student_semester_db,
                                      view_students_filtered,
                                      view_student_by_id
                                      )
import exceptions 

def add_student(name,department,semester):
    if semester<1 or semester>8:
        raise exceptions.ValidationError("Semester must be between 1 and 8.")
    else:
        return create_student(name,department,semester)
    
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

def get_students_filtered(department,semester,page,page_size):
    if page<1:
        raise exceptions.ValidationError("Number of pages must be minimum 1.")
    if page_size<1:
        raise exceptions.ValidationError("Page size must be minimum 1")
    x=view_students_filtered(department,semester,page,page_size)
    return x
