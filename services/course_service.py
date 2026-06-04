from database import get_db_connection
from models.course import Course

def add_course(course_name,credits):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into courses(course_name,credits)values(?,?)""",(course_name,credits))
    conn.commit()
    course_id=cursor.lastrowid
    course=Course(course_id,course_name,credits)
    conn.close()

    return course

def get_all_courses():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from courses""")
    rows=cursor.fetchall()
    conn.close()
    courses=[Course(*row) for row in rows]
    return courses

def delete_course(course_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""delete from courses where id=?""",(course_id,))
    conn.commit()
    affected_rows=cursor.rowcount
    conn.close()
    return affected_rows>0