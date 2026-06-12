from database import(create_slot,
                     view_all_slots,
                     view_slot_by_id,
                     view_all_slots_day_room,
                     view_all_slots_day,
                     delete_slot)
from exceptions import(ValidationError,
                       ResourceNotFoundError)
from database import view_course_by_id

def add_slot(course_id,day,start_time,end_time,room):
    if start_time>=end_time:
        raise ValidationError("Start time should be before end time.")
    if not view_course_by_id(course_id):
        raise ValidationError(f"Course does not exists with id {course_id}")
    slot=view_all_slots_day_room(day,room)
    for i in slot:
        if start_time<i.end_time and end_time>i.start_time:
            raise ValidationError(f"Slot from {start_time} to {end_time} already occupied. ")
    slot_id=create_slot(course_id,day,start_time,end_time,room)

    if not slot_id:
        raise ValidationError("Slot unable to create.")
    return slot_id

def get_all_slots_ser():
    slots=view_all_slots()
    if not slots:
        raise ResourceNotFoundError("No slot found.")
    return slots

def get_slot(id):
    slot=view_slot_by_id(id)
    if not slot:
        raise ResourceNotFoundError("No slot found.")
    return slot

def remove_slot(id):
    slot=delete_slot(id)
    if not slot:
        raise ResourceNotFoundError("No slot found.")
    return slot

def get_slots_by_day(day):
    slots=view_all_slots_day(day)
    if not slots:
        raise ValidationError(f"No slots filled for {day}")
    return slots



