from datetime import datetime
from database import(create_notice,
                     get_all_notices,
                     get_notice_by_id,
                     delete_notice
                     )
from exceptions import(ValidationError,
                       ResourceNotFoundError) 
def add_notice(title,content):
    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row=create_notice(title,content,created_at)
    if not row:
        raise ValidationError("Notice not created.")
    return row

def view_all_notice():
    notices=get_all_notices()
    if not notices:
        raise ResourceNotFoundError("No notices found.")
    return notices
    
def view_notice_by_id(id):
    notice=get_notice_by_id(id)
    if not notice:
        raise ResourceNotFoundError("Notice not found.")
    return notice
    
def remove_notice(id):
    notice=delete_notice(id)
    if not notice:
        raise ResourceNotFoundError("Notice not found.")
    return notice
