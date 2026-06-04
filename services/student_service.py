from database import get_db_connection
from models.student import Student

def add_student(name,department,semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    if semester<1 or semester>8:
        raise ValueError("Semester must be between 1 and 8.")
    cursor.execute("""insert into students(name,department,semester)
                   values(?,?,?)""",(name,department,semester))
    
    conn.commit()
    student_id=cursor.lastrowid
    conn.close()
    return Student(student_id,name,department,semester)

def get_all_students():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("select id,name,department,semester from students")
    rows=cursor.fetchall()
    conn.close()
    students=[Student(*row) for row in rows]
    return students

def update_student(student_id,name,department,semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""update students set name=? , department=? , semester=? where id=?""",(name,department,semester,student_id))
    conn.commit()
    rows_affected=cursor.rowcount
    conn.close()
    return rows_affected > 0

def delete_student(student_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""delete from students where id=?""",
                   (student_id,))
    conn.commit()
    row_count=cursor.rowcount
    conn.close()
    return row_count > 0

def get_student_by_department(department):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from students where department=?""",(department,))
    rows=cursor.fetchall()
    conn.close()
    students=[Student(*row) for row in rows]
    return students

def get_students_by_semester(semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from students where semester=?""",(semester,))
    rows=cursor.fetchall()
    conn.close()
    students=[Student(*row) for row in rows]
    return students


def get_students_by_department_and_semester(department=None,semester=None):
    conn=get_db_connection()
    cursor=conn.cursor()
    query="select * from students where 1=1"
    params=[]

    if department:
        query+=" and department=?"
        params.append(department)

    if semester:
        query+=" and semester=?"
        params.append(semester)

    cursor.execute(query,tuple(params))
    rows=cursor.fetchall()
    conn.close()
    students=[Student(*row) for row in rows]
    return students

def get_student_by_id(student_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""Select * from students where id=?""",(student_id,))
    row=cursor.fetchone()
    if row:
        return Student(*row)
    cursor.close()
    conn.close()
    return None

def update_student_semester(semester,student_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    if semester < 1 or semester > 8:
        raise ValueError("Semester must be between 1 and 8.")
    cursor.execute("""Update students set semester=? where id=?""",(semester,student_id))
    conn.commit()
    row=cursor.fetchone()
    if row:
        return True
    cursor.close()
    conn.close()
    return False