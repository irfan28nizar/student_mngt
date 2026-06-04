class Course:
    def __init__(self,course_id,course_name,credits):
        self.course_id=course_id
        self.course_name=course_name
        self.credits=credits
    def __repr__(self):
        return (
        f"Course_id={self.course_id},"
        f"Course_name={self.course_name}, " 
        f"Credits={self.credits})")