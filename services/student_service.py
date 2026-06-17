from database import (create_student,
                                      delete_student,
                                      update_student_semester_db,
                                      view_students_filtered,
                                      view_student_by_id
                                      )
import exceptions 
from validators import(is_int,is_valid_data)
def add_student(name,department,semester):
    if not is_valid_data(name):
        raise exceptions.ValidationError("name is required.")
    if not is_valid_data(department):
        raise exceptions.ValidationError("department is required.")
    if not is_int(semester):
        raise exceptions.ValidationError("semester must be integer.")
    if not len(name)<=100:
        raise exceptions.ValidationError("Maximum length of name is 100")
    if not len(department)<=100:
        raise exceptions.ValidationError("Maximum length of department is 100")
    if semester<1 or semester>8:
        raise exceptions.ValidationError("Semester must be between 1 and 8.")
    return create_student(name,department,semester)
    
def get_student_by_id(student_id):
    if not is_int(student_id):
        raise exceptions.ValidationError("Student id must be integer")
    x=view_student_by_id(student_id)
    if not x:
        raise exceptions.ResourceNotFoundError("Student not found.")
    return x

def update_student(semester,student_id):
    if not is_int(student_id):
        raise exceptions.ValidationError("studeent_id must be integer")
    if not is_int(semester):
        raise exceptions.ValidationError("semester must be integer.")
    if semester < 1 or semester > 8:
        raise exceptions.ValidationError("Semester must be between 1 and 8.")
    temp=get_student_by_id(student_id)
    if not temp:
        raise exceptions.ValidationError(f"Student with id{student_id} not found.")
    else:
        return update_student_semester_db(semester,student_id)
    

def remove_student(student_id):
    if not is_int(student_id):
        raise exceptions.ValidationError("student id must be integer.")
    if not get_student_by_id(student_id):    
        raise exceptions.ResourceNotFoundError("Student not found.")
    return delete_student(student_id)

def get_students_filtered(department,semester,page,page_size):
    if not 1<page<1000:
        raise exceptions.ValidationError("Number of pages must be between 1 and 1000 .")
    if not 1<page_size<1000:
        raise exceptions.ValidationError("Page size must be between 1 and 100")
    x=view_students_filtered(department,semester,page,page_size)
    return x
