class Student:
    def __init__(self,student_id,name,department,semester):
        self.student_id=student_id
        self.name=name
        self.department=department  
        self.semester=semester

    def __repr__(self):
        return (
        f"Student(id={self.student_id},"
        f"name={self.name}, " 
        f"department={self.department}, " 
        f"semester={self.semester})")
    
    def student_to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "department": self.department,
            "semester": self.semester
        }
    
