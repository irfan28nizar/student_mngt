from database import(create_course,
                    delete_course,view_course_by_id,
                    view_course_by_name,
                    view_all_courses)
from exceptions import(ValidationError,
                       ResourceNotFoundError) 
from validators import is_int,is_valid_data

def add_course(course_name,credits):
    if not is_valid_data(course_name):
        raise ValidationError("Course name is required.")
    if not is_int(credits):
        raise ValidationError("credits must be integer")
    if not 0<=credits<=4:
        raise ValidationError("Credits must be between 0 and 4.")
    x=view_course_by_name(course_name.strip())
    if x:
        raise ValidationError(f"Course already exists with id {x.course_id}. ")
    return create_course(course_name.strip(),credits)
    

def get_all_courses():
    courses=view_all_courses()
    return courses

def get_course_by_id(course_id):
    if not is_int(course_id):
        raise ValidationError("Course id must be integer.")
    courses=view_course_by_id(id)
    if not courses:
        raise ResourceNotFoundError("No course found.")
    return courses

def remove_course(course_id): 
    if not is_int(course_id):
        raise ValidationError("Course id must be integer.")  
    course=view_course_by_id(course_id)
    if not course:
        raise ResourceNotFoundError("No course found.")
    return delete_course(course_id)