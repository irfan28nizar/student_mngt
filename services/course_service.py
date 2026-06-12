from database import(create_course,
                    delete_course,view_course_by_id,
                    view_course_by_name,
                    view_all_courses)
from exceptions import(ValidationError,
                       ResourceNotFoundError) 

def add_course(course_name,credits):
    if credits>4:
        raise ValidationError("Maximum credits is 4.")
    x=view_course_by_name(course_name)
    if x:
        raise ValidationError(f"Course already exists with id{x.course_id}. ")
    course=create_course(course_name,credits)
    if not course:
        raise ValidationError("Course not created.")
    return course

def get_all_courses():
    courses=view_all_courses()
    if not courses:
        raise ResourceNotFoundError("No courses found.")
    return courses

def get_course_by_id(id):
    courses=view_course_by_id(id)
    if not courses:
        raise ResourceNotFoundError("No course found.")
    return courses

def remove_course(course_id):   
    course=delete_course(course_id)
    if not course:
        raise ResourceNotFoundError("No course found.")
    return course