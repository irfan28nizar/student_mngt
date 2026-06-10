import sqlite3
from models.student import Student
from models.course import Course
from models.admin import Admin
db_name="student_management.db"

def get_db_connection():
    conn=sqlite3.connect(db_name)
    return conn.cursor()
#TABLES

def create_tables():
    conn=get_db_connection()
    cursor=conn.cursor()

    cursor.execute("""create table if not exists students(
                   id integer primary key autoincrement ,
                    name text not null , 
                   department text not null , 
                   semester integer not null)""")
    cursor.execute("""create table if not exists courses(
                   id integer primary key autoincrement , 
                   course_name text not null , 
                   credits integer not null)""")
    cursor.execute("""create table if not exists admin(
                    id integer primary key autoincrement ,
                    username text not null ,
                    password_hash text not null)""")

    conn.commit()
    conn.close()

#STUDENT CRUD OPERATIONS

def create_student(name,department,semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into students(name,department,semester)
                   values(?,?,?)""",(name,department,semester))
    conn.commit()
    student_id=cursor.lastrowid
    conn.close()
    return Student(student_id,name,department,semester)

def view_all_students():
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

def view_student_by_department(department):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from students where department=?""",(department,))
    rows=cursor.fetchall()
    conn.close()
    students=[Student(*row) for row in rows]
    return students

def view_students_by_semester(semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from students where semester=?""",(semester,))
    rows=cursor.fetchall()
    conn.close()
    students=[Student(*row) for row in rows]
    return students


def view_students_by_department_and_semester(department=None,semester=None):
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

def view_student_by_id(student_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""Select * from students where id=?""",(student_id,))
    row=cursor.fetchone()
    if row:
        return Student(*row)
    cursor.close()
    conn.close()
    return None

def update_student_semester_db(semester,student_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""Update students set semester=? where id=?""",(semester,student_id))
    conn.commit()
    row=cursor.fetchone()
    if row:
        return True
    cursor.close()
    conn.close()
    return False

#COURSE CRUD OPERATIONS


def create_course(course_name,credits):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into courses(course_name,credits)values(?,?)""",(course_name,credits))
    conn.commit()
    course_id=cursor.lastrowid
    course=Course(course_id,course_name,credits)
    conn.close()

    return course

def view_all_courses():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from courses""")
    rows=cursor.fetchall()
    conn.close()
    courses=[Course(*row) for row in rows]
    return courses

def remove_course(course_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""delete from courses where id=?""",(course_id,))
    conn.commit()
    affected_rows=cursor.rowcount
    conn.close()
    return affected_rows>0

#ADMIN CRUD OPERATIONS

def create_admin(username,password):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(""""insert into admin (username,password_hash) values(?,?) """,(username,password))
    conn.commit()
    admin_id=cursor.lastrowid
    conn.close()
    return admin_id

def get_admin_by_username(username):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from admin where username=?""",(username,))
    row=cursor.fetchone()
    conn.close()
    return Admin(*row) if row else None
