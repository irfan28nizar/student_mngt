import sqlite3
conn=sqlite3.connect("trial.db")
cursor=conn.cursor()
cursor.execute("""create table if not exists trial(id integer primary key autoincrement,name text not null)""")

name=input("enter name:")


query = f"""
SELECT * FROM trial
WHERE name='{name}'
"""

print(query)
cursor.execute(query)

row=cursor.fetchall()
conn.commit()
cursor.close()
conn.close()
print(row)
