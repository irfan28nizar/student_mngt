from flask import Flask, jsonify , request
from database import create_tables
from validators import checkpass

import exceptions
app=Flask(__name__)
create_tables()  
@app.route("/")
def home():
    return{"message":"Backend Working"}

#Global Error Handler
@app.errorhandler(exceptions.ValidationError)
def handle_validation_error(error):
    return {"error":str(error)},400

@app.errorhandler(exceptions.AuthenticationError)
def handle_authentication_error(error):
    return{"error":str(error)},401

@app.errorhandler(exceptions.ResourceNotFoundError)
def handle_resource_not_found_error(error):
    return {"error":str(error)},404


#STUDENT ROUTES
from services.student_service import(update_student,
                                     get_student_by_id,
                                     get_students_filtered,
                                     add_student,
                                     remove_student)

@app.route("/students",methods=["GET"])
def api_view_students():
    department=request.args.get("department")
    semester=request.args.get("semester",type=int)
    page=request.args.get("page",default=1,type=int)
    page_size=request.args.get("page_size",default=10,type=int)
    students=get_students_filtered(department,semester,page,page_size)
    return jsonify([student.student_to_dict()
        for student in students
    ])

@app.route("/students",methods=["POST"])
def api_create_student():
    data=request.get_json()
    if not data:
        return {"error":"JSON data required"},400
    if "name" not in data:
        return {"error":"Name is required"},400
    if "department" not in data:
        return {"error":"Department is required"},400
    if "semester" not in data:
        return {"error":"Semester is required"},400
    add_student(data["name"],data["department"],int(data["semester"]))
    return {"message":"Student Created"},201

@app.route("/students/<int:student_id>",methods=["GET"])
def api_get_student(student_id):
    student=get_student_by_id(student_id)
    return jsonify(student.student_to_dict()),200

@app.route("/students/<int:student_id>",methods=["PATCH"])
def api_update_student_by_semester(student_id):
    data=request.get_json()
    if "semester" not in data:
        return {"error":"Semester is required"},400
    if update_student(data["semester"],student_id):
        return {"message":"Student semester updated"},200
    
@app.route("/students/<int:student_id>",methods=["DELETE"])
def api_delete_std_id(student_id):
        remove_student(student_id)
        return {"message":"Student deleted"},200
    
#COURSE ROUTE
from services.course_service import(add_course,
                                    get_all_courses,
                                    get_course_by_id,
                                    remove_course)
@app.route("/courses",methods=["POST"])
def api_new_course():
    data=request.get_json()
    if not data:
        return {"error":"JSON data required"},400
    if "course_name" not in data:
        return {"error":"Course name is required."},400
    if "credits" not in data:
        return{"error":"credits is required"},400
    x=add_course(data["course_name"],data["credits"])
    if x:
        return {"message":f"Course created with slot_id {x}."},201

@app.route("/courses",methods=["GET"])
def api_view_all_cou():
    courses=get_all_courses()
    return jsonify([course.course_to_dict()
        for course in courses]),200
    
@app.route("/courses/<int:course_id>",methods=["GET"])
def api_get_cou_id(course_id):
    course=get_course_by_id(course_id)
    return jsonify(course.course_to_dict()),200    
    
@app.route("/courses/<int:slot_id>",methods=["DELETE"])
def api_del_cou_id(slot_id):
    remove_course(slot_id)
    return {"message":f"Course slot_id={slot_id} deleted."},200
    
    
#ADMIN ROUTES
from services.admin_services import (register_admin,
                                      login_admin)

@app.route("/register",methods=["POST"])
def api_register():
    data=request.get_json()
    if not data:
        return {"error":"JSON data required."},400
    if "username" not in data:
        return {"error":"username is required."},400
    if "password" not in data:
        return{"error":"Password is required"},400
    if register_admin(data["username"],data["password"]):
        return {"message":"Admin registered successfully"},201

@app.route("/login",methods=["POST"])
def api_login():
    data=request.get_json()
    if not data:
        return {"error":"JSON data required."},400
    if "username" not in data:
        return{"error":"Username is required"},400
    if "password" not in data:
        return{"error":"Password is required"},400
    if login_admin(data["username"],data["password"]):
        return{"message":"Login Successful"},200

#NOTICES ROUTES

from services.notice_services import(add_notice,
                                     get_all_notice,
                                     get_notice_by_id,
                                     remove_notice,
restore_notice_id
                                     )


@app.route("/notices",methods=["POST"])
def api_add_notice():
    data=request.get_json()
    if not data:
        return {"error":"JSON data required."},400
    if "title" not in data:
        return{"error":"Title cannot be empty."},400
    if "content" not in data:
        return{"error":"Content cannot be empty."},400
    add_notice(data["title"],data["content"])
    return {"message":"Notice created"},201
    
@app.route("/notices",methods=["GET"])
def api_view_all_notice():
    notices=get_all_notice()
    return jsonify([
        notice.notice_to_dict()
    for notice in notices
    ]),200

@app.route("/notices/<int:slot_id>",methods=["GET"])
def api_get_notice_by_id(slot_id):
    notice=get_notice_by_id(slot_id)
    return jsonify(notice.notice_to_dict()),200

@app.route("/notices/<int:slot_id>",methods=["PATCH"])
def api_soft_del_notice(slot_id):
    remove_notice(slot_id)
    return {"message":"Notice deleted."},200
    
@app.route("/notices/<int:slot_id>/restore",methods=["PATCH"])
def api_restore_notice(slot_id):
    restore_notice_id(slot_id)
    return{"message":"Notice activated."},200


    
#TIMETABLE ROUTES

from services.timetable_service import(add_slot,
                               get_all_slots_ser,
                               get_slot_by_course_id,
                               remove_slot,
                               get_slots_by_day)
@app.route("/timetable",methods=["POST"])
def api_new_slot():
    data=request.get_json()
    if not data:
        return {"error":"JSON data required."},400
    if "course_id" not in data:
        return {"error":"course_id is required"},400
    if "day" not in data:
        return {"error":"day required"},400
    if "start_time" not in data:
        return {"error":"start_time required"},400
    if "end_time" not in data:
        return {"error":"end_time required"},400
    if "room" not in data:
        return {"error":"room_id required"},400
    add_slot(data["course_id"],data["day"],data["start_time"],data["end_time"],data["room"])
    return {"message":"Slot created"},201
    
@app.route("/timetable",methods=["GET"])   
def api_get_all_slot():
    day=request.args.get("day",default=None)
    course_id=request.args.get("course_id",default=None,type=int)
    room=request.args.get("room",default=None)
    page=request.args.get("page",default=1,type=int)
    page_size=request.args.get("page_size",default=10,type=int)
    slots=get_all_slots_ser(course_id,day,room,page,page_size)
    return jsonify([slot.timetable_to_dict()
                         for slot in slots]),200

@app.route("/timetable/<int:course_id>/slots",methods=["GET"])
def api_get_slots_by_cou_id(course_id):
    slots=get_slot_by_course_id(course_id)
    return jsonify([slot.timetable_to_dict()
        for slot in slots]),200
    
@app.route("/timetable/<int:slot_id>",methods=["DELETE"])
def api_del_slot(slot_id):
    dell=remove_slot(slot_id)
    return {"message":f"{dell} deleted"},200
    
@app.route("/timetable/day/<day>",methods=["GET"])
def api_get_slots_by_day(day):       #1
    slots=get_slots_by_day(day)
    return jsonify([
        slot.timetable_to_dict()   
        for slot in slots])

if __name__ == "__main__":
    app.run(debug=True)

