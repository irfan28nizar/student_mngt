class Timetable:
    def __init__(self,id,course_id,day,start_time,end_time,room):
        self.id=id
        self.course_id=course_id
        self.day=day
        self.start_time=start_time
        self.end_time=end_time
        self.room=room

    def __repr__(self):
        return ("Timetable("f"id:{self.id},"
                f"course_id:{self.course_id},"
                f"day:{self.day},"
                f"start_time:{self.start_time},"
                f"end_time:{self.end_time},"
                f"room:{self.room}")
    
    def timetable_to_dict(self):
        return {
            "id":self.id,
        "course_id":self.course_id,
        "day":self.day,
        "start_time":self.start_time,
        "end_time":self.end_time,
        "room":self.room 
        }
    
    