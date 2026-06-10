from database import(create_course,
                    remove_course,
                    view_all_courses)

def add_course(course_name,credits):
    return create_course(course_name,credits)

def get_all_courses():
    return view_all_courses()

def delete_course(course_id):   
    return remove_course(course_id)
