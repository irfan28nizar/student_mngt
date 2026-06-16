from datetime import datetime
from database import(create_notice,
                     view_all_notices,
                     view_notice_by_id,
                     delete_notice,
                     restore_notice,
                     check_notice
                     )
from exceptions import(ValidationError,
                       ResourceNotFoundError) 
from validators import is_int,is_valid_data,lengthcheck
def add_notice(title,content):
    if not is_valid_data(title):
        raise ValidationError("Title is required.")
    if not is_valid_data(content):
        raise ValidationError("Content is required.")
    if not len(title)<=100:
        raise ValidationError("Maximum length of title is 100")
    if not lengthcheck(content):
        raise ValidationError("Content length must be atleast 25 characters.")
    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return create_notice(title,content,created_at)

def get_all_notice():
    return view_all_notices()
    
def get_notice_by_id(notice_id):
    if not is_int(notice_id):
        raise ValidationError("Notice id must be integer.")
    notice=view_notice_by_id(notice_id)
    if not notice:
        raise ResourceNotFoundError("Notice not found.")
    return notice
    
def remove_notice(notice_id):
    if not is_int(notice_id):
        raise ValidationError("Notice id must be integer.")
    if not get_notice_by_id(notice_id):
        raise ResourceNotFoundError("Notice not found.")
    return delete_notice(notice_id)


def restore_notice_id(notice_id):
    if not is_int(notice_id):
        raise ValidationError("Notice id must be integer.")
    info=check_notice(notice_id)
    if not info:
        raise ResourceNotFoundError("Notice not found.")
    if info.is_deleted==0:
        raise ValidationError("Notice already active.")
    return restore_notice(notice_id)
    
