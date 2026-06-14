from database import(create_slot,
                     view_all_slots,
                     view_slot_by_courseid,
                     view_all_slots_day_room,
                     view_all_slots_day,
                     view_by_slot_id,
                     delete_slot)
from exceptions import(ValidationError,
                       ResourceNotFoundError)
from database import view_course_by_id
from validators import(is_int,
                       is_valid_data,
                       check_weekdays)
def add_slot(course_id,day,start_time,end_time,room):
    if not is_int(course_id):
        raise ValidationError("Course_id must be integer.")
    if not is_valid_data(day):
        raise ValidationError("Day is required.")
    if not check_weekdays(day):
        raise ValidationError(f"{day} is not a weekday.")
    if not is_valid_data(start_time):
        raise ValidationError("start time is required.")
    if not is_valid_data(end_time):
        raise ValidationError("end time is required.")
    if not is_valid_data(room):
        raise ValidationError("room number is required.")
    if start_time>=end_time:
        raise ValidationError("Start time should be before end time.")
    if not view_course_by_id(course_id):
        raise ValidationError(f"Course does not exists with slot_id {course_id}")
    slot=view_all_slots_day_room(day,room)
    for i in slot:
        if start_time<i.end_time and end_time>i.start_time:
            raise ValidationError(f"Slot from {start_time} to {end_time} already occupied. ")
    return create_slot(course_id,day,start_time,end_time,room)

def get_all_slots_ser(course_id,day,room,page,page_size):
    if page<1:
        raise ValidationError("Number of pages must be minimum 1.")
    if page_size<1:
        raise ValidationError("Page size must be minimum 1")
    return view_all_slots(course_id,day,room,page,page_size)
   

def get_slot_by_course_id(course_id):
    if not is_int(course_id):
        raise ValidationError("Course_id must be integer.")
    slot=view_slot_by_courseid(course_id)
    if not slot:
        raise ResourceNotFoundError("No slot found.")
    return slot

def remove_slot(slot_id):
    if not is_int(slot_id):
        raise ValidationError("Slot id must be integer.")
    if not view_by_slot_id(slot_id):
        raise ResourceNotFoundError("No slot found.")
    return delete_slot(slot_id)

def get_slots_by_day(day):
    if not is_valid_data(day):
        raise ValidationError("Day is required.")
    if not check_weekdays(day):
        raise ValidationError(f"{day} is not a weekday.")
    slots=view_all_slots_day(day)
    if not slots:
        raise ValidationError(f"No slots filled for {day}")
    return slots



