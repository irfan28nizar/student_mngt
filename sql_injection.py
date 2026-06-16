# import sqlite3
# conn=sqlite3.connect("trial.db")
# cursor=conn.cursor()
# cursor.execute("""create table if not exists trial(id integer primary key autoincrement,name text not null)""")

# name=input("enter name:")


# query = f"""
# SELECT * FROM trial
# WHERE name='{name}'
# """

# print(query)
# cursor.execute(query)

# row=cursor.fetchall()
# conn.commit()
# cursor.close()
# conn.close()
# print(row)
# inp=int(input("enter:"))
# l=[]
# j=[]
# for i in range(inp):
#     read=str(input())
#     l.append(read.split())

# for i in l:
   
#     if "append" in i:
#         j.append(int(i[1]))
#     elif "insert" in i:
#         j.insert(int(i[1]),int(i[2]))
#     elif "remove" in i:
#         j.remove(int(i[1]))
#     elif "print" in i:
#         print(j)
#     elif "sort" in i:
#         j.sort()
#     elif "pop" in i:
#         j.pop()
#     elif "reverse" in i:
#         j.reverse()
#     else:
#         pass
# arr=[1,2,3,4]
# l=len(arr)
# print(arr[l-1])


