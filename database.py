import sqlite3
from models.student import Student
from models.course import Course
from models.admin import Admin
from models.notices import Notice
db_name="database.db"



def get_db_connection():
    conn=sqlite3.connect(db_name)
    return conn

#CHANGES AND TESTING

# conn=get_db_connection()
# cursor=conn.cursor()
# cursor.execute("""alter table notices add column is_deleted not null default 0 """)
# conn.commit()
# cursor.execute("""select * from notices""")
# row=cursor.fetchall()
# print(row)
# cursor.close()
# conn.close()


#TABLES
def create_tables():
    conn=get_db_connection()
    cursor=conn.cursor()
    conn.execute("PRAGMA foreign_keys = ON")

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
    cursor.execute("""create table if not exists notices(
                   id integer primary key autoincrement,
                   title text not null ,
                   content text not null , 
                   created_at text not null)""")
    cursor.execute("""create table if not exists timetable(
               id integer primary key autoincrement,
               course_id integer not null,
               day text not null,
               start_time text not null,
               end_time text not null,
                room text not null,
               foreign key(course_id) references courses(id)) """)
    conn.commit()
    cursor.close()
    conn.close()

#STUDENT CRUD OPERATIONS

def create_student(name,department,semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into students(name,department,semester)
                   values(?,?,?)""",(name,department,semester))
    conn.commit()
    student_id=cursor.lastrowid
    cursor.close()
    conn.close()
    return Student(student_id,name,department,semester)


def update_student(student_id,name,department,semester):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""update students set name=? , department=? , semester=? where id=?""",(name,department,semester,student_id))
    conn.commit()
    rows_affected=cursor.rowcount
    cursor.close()
    conn.close()
    return rows_affected > 0

def delete_student(student_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""delete from students where id=?""",
                   (student_id,))
    conn.commit()
    row_count=cursor.rowcount
    cursor.close()
    conn.close()
    return row_count > 0

def view_students_filtered(department,semester,page,page_size):
    conn=get_db_connection()
    cursor=conn.cursor()
    offset=(page-1)*page_size
    query="select * from students where 1=1"
    params=[]

    if department:
        query+=" and department=?"
        params.append(department)

    if semester:
        query+=" and semester=?"
        params.append(semester)
    query+=" order by name asc limit ? offset ? "
    params.append(page_size)
    params.append(offset)

    cursor.execute(query,tuple(params))
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    if not rows:
        return[]
    return [Student(*row) for row in rows]

def view_students_paginated(page,page_size):
    offset=(page-1)*page_size
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from students limit ? offset ?""",(page_size,offset))
    students=cursor.fetchall()
    cursor.close()
    conn.close()
    if not students:
        return []
    return [Student(*row) for row in students]

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
    row=cursor.rowcount
    cursor.close()
    conn.close()
    return row >0

#COURSE CRUD OPERATIONS
from models.course import Course

def create_course(course_name,credits):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into courses(course_name,credits)values(?,?)""",(course_name,credits))
    conn.commit()
    course_id=cursor.lastrowid
    cursor.close()
    conn.close()
    return course_id

def view_all_courses():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from courses""")
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    if not rows:
        return []
    return [Course(*row) for row in rows]

def view_course_by_id(course_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from courses where id=?""",(course_id,))
    rows=cursor.fetchone()
    cursor.close()
    conn.close()
    return Course(*rows) if rows else None

def view_course_by_name(course_name):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from courses where course_name=?""",(course_name,))
    rows=cursor.fetchone()
    cursor.close()
    conn.close()
    return Course(*rows) if rows else None 


def delete_course(course_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""delete from courses where id=?""",(course_id,))
    conn.commit()
    affected_rows=cursor.rowcount
    cursor.close()
    conn.close()
    return affected_rows>0

#ADMIN CRUD OPERATIONS

def create_admin(username,password):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into admin (username,password_hash) values(?,?) """,(username,password))
    conn.commit()
    admin_id=cursor.lastrowid
    cursor.close()
    conn.close()
    return admin_id

def view_admin_by_username(username):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from admin where username=?""",(username,))
    row=cursor.fetchone()
    cursor.close()
    conn.close()
    return Admin(*row) if row else None

#NOTICE CRUD OPERATIONS
def create_notice(title,content,created_at):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into notices(title,content,created_at)values(?,?,?)""",(title,content,created_at))
    conn.commit()
    row=cursor.rowcount
    cursor.close()
    conn.close()
    return row > 0

def view_all_notices():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from notices where is_deleted=?""",(0,))
    notices=cursor.fetchall()
    cursor.close()
    conn.close()
    return [Notice(*notice)for notice in notices]

def view_notice_by_id(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from notices where id=? and is_deleted=?""",(id,0))
    row=cursor.fetchone()
    cursor.close()
    conn.close()
    return Notice(*row) if row else None

def delete_notice(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(""" update notices set is_deleted=? where id=?""",(1,id))
    conn.commit()
    row=cursor.rowcount
    cursor.close()
    conn.close()
    return row>0

def restore_notice(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(""" update notices set is_deleted=? where id=?""",(0,id))
    conn.commit()
    row=cursor.rowcount
    cursor.close()
    conn.close()
    return row>0

def check_notice(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(""" select * from notices where id=?""",(id,))
    row=cursor.fetchone()
    cursor.close()
    conn.close()
    return Notice(*row) if row else None
    
#timetable 
from models.timtetable import Timetable
def create_slot(course_id,day,start_time,end_time,room):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""insert into timetable(course_id,
                   day,
                   start_time,
                   end_time,
                   room)values(?,?,?,?,?)""",(course_id,day,start_time,end_time,room))
    conn.commit()
    slot=cursor.lastrowid
    cursor.close()
    conn.close()
    return slot

def view_all_slots(course_id,day,room,page,page_size):
    conn=get_db_connection()
    cursor=conn.cursor()
    offset=(page-1)*page_size
    query=("select * from timetable where 1=1")
    params=[]
    if course_id:
        query+=" and course_id=?"
        params.append(course_id)
    if day:
        query+=" and day=?"
        params.append(day)
    if room:
        query+=" and room=?"
        params.append(room)

    query+=" limit ? offset ?"
    params.append(page_size)
    params.append(offset)
    cursor.execute(query,tuple(params))
    all_slot=cursor.fetchall()
    cursor.close()
    conn.close()
    return [Timetable(*slot) for slot in all_slot]
    
def view_slot_by_courseid(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from timetable where course_id=?""",(id,))
    slots=cursor.fetchall()    
    cursor.close()
    conn.close()
    if not slots:
        return []
    return [Timetable(*slot) for slot in slots]

def delete_slot(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""delete from timetable where id=?""",(id,))
    count=cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    if count>0:
        return count
    
def view_slot_details(day,start_time,end_time,room):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from timetable where day=? and start_time=? and end_time=? and room=? """,(day,start_time,end_time,room))
    row=cursor.fetchone()
    cursor.close()
    conn.close()
    return Timetable(*row) if row else None
    
def view_all_slots_day_room(day,room):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from timetable where day=? and room=? """,(day,room))
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    if rows:
        return [Timetable(*row) for row in rows]
    else:
        return []
    
def view_all_slots_day(day):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from timetable where day=? order by start_time """,(day,))
    rows=cursor.fetchall()
    cursor.close()
    conn.close()
    if rows:
        return [Timetable(*row) for row in rows]
    else:
        return []
    
def view_by_slot_id(slot_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""select * from timetable where id=?""",(slot_id,))
    count=cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return count
    

    