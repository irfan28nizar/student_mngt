import sqlite3
db_name="student_management.db"

def get_db_connection():
    return sqlite3.connect(db_name)

def create_tables():
    conn=get_db_connection()
    cursor=conn.cursor()

    cursor.execute("""create table if not exists students(
                   id integer primary key autoincrement ,
                    name text not null , 
                   department text not null , 
                   semester integer not null)""")
    
    #done

    cursor.execute("""create table if not exists courses(
                   id integer primary key autoincrement , 
                   course_name text not null , 
                   credits integer not null)""")
    
    #done

    cursor.execute("""create table if not exists enrollments(
                   student_id integer , 
                   course_id integer , 
                   primary key(student_id, course_id) , 
                   foreign key(student_id) references students(id), 
                   foreign key(course_id) references courses(id) )""")
    
    cursor.execute("""create table if not exists grades(student_id integer ,
                   course_id integer ,
                   marks real ,
                   primary key(student_id, course_id) ,
                   foreign key(student_id) references students(id),
                   foreign key(course_id) references courses(id)
                   )""")
    
    conn.commit()
    conn.close()

