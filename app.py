from flask import Flask, jsonify , request
from database import create_tables
from services.admin_services import (register_admin,
                                      login_admin)
from validators import checkpass
from services.student_service import update_student, get_student_by_id,get_all_students,add_student
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

@app.route("/students",methods=["GET"])
def api_view_students():
    students=get_all_students()
    return jsonify([
        {
            "id":student.student_id,
            "name":student.name,
            "department":student.department,
            "semester":student.semester
        }
        for student in students
    ])

@app.route("/students",methods=["POST"])
def api_create_student():
    data=request.get_json()
    if not data["name"].strip():
        return {"error":"Name is required"},400
    if not data["department"].strip():
        return {"error":"Department is required"},400
    if not isinstance(data["semester"],int):
        return {"error":"Semester must be an integer"},400
    add_student(data["name"],data["department"],int(data["semester"]))
    return {"message":"Student Created"},201

@app.route("/students/<int:student_id>",methods=["GET"])
def api_get_student(student_id):
    student=get_student_by_id(student_id)
    if student:
        return jsonify({
            "id":student.student_id,
            "name":student.name,
            "department":student.department,
            "semester":student.semester
        }),200

@app.route("/students/<int:student_id>",methods=["PATCH"])
def api_update_student_by_semester(student_id):
    data=request.get_json()
    if "semester" not in data:
        return {"error":"Semester is required"},400
    if not isinstance(data["semester"],int):
        return {"error":"Semester must be an integer"},400
    
    if update_student(data["semester"],student_id):
        return {"message":"Student semester updated"},200
    else:
        return {"error":"Failed to update student semester"},404
    
#COURSE ROUTE
from services.course_service import(add_course,
                                    get_all_courses,
                                    get_course_by_id,
                                    remove_course)
@app.route("/course",methods=["POST"])
def api_new_course():
    data=request.get_json()
    if not data["course_name"]:
        return {"error":"Course name is required."},400
    if not isinstance(data["credits"],int):
        return {"error":"Credits must be integer"},400
    x=add_course(data["course_name"],data["credits"])
    if x:
        return {"message":f"Course created with id {x}."},201

@app.route("/course",methods=["GET"])
def api_view_all_cou():
    courses=get_all_courses()
    if courses:
        return jsonify([{
            "id":course.course_id,
            "course_name":course.course_name,
            "credits":course.credits
        }
        for course in courses])
    
@app.route("/course/<int:id>",methods=["GET"])
def api_get_cou_id(id):
    course=get_course_by_id(id)
    if course:
        return jsonify({
            "id":course.course_id,
            "course_name":course.course_name,
            "credits":course.credits
        }),200    
    
@app.route("/course/<int:id>",methods=["DELETE"])
def api_del_cou_id(id):
    course=remove_course(id)
    if course:
        return {"message":f"Course id={id} deleted."},200
    
    
#ADMIN ROUTES

@app.route("/register",methods=["POST"])
def api_register():
    data=request.get_json()
    if not data["username"].strip():
        return{"error":"Username is required"},400
    if not data["password"].strip():
        return{"error":"Password is required"},400
    if not checkpass(data["password"]):
        return{"error":"Password must be at least 8 characters long,"
        " contain a number, an uppercase letter,"
        " a lowercase letter, and a special character"},400
    admin=register_admin(data["username"],data["password"])
    if admin:
        return {"message":"Admin registered successfully"},201

@app.route("/login",methods=["POST"])
def api_login():
    data=request.get_json()
    if not data["username"].strip():
        return{"error":"Username is required"},400
    if not data["password"].strip():
        return{"error":"Password is required"},400
    if login_admin(data["username"],data["password"]):
        return{"message":"Login Successful"},200

#NOTICES ROUTES

from services.notice_services import(add_notice,
                                     get_all_notice,
                                     get_notice_by_id,
                                     remove_notice
                                     )

from validators import lengthcheck

@app.route("/notices",methods=["POST"])
def api_add_notice():
    data=request.get_json()
    if not data["title"].strip():
        return{"error":"Title cannot be empty."},400
    if not data["content"].strip():
        return{"error":"Content cannot be empty."},400
    if not lengthcheck(data["content"]):
        return{"error":"Content length must be 25 characters."},400
    if add_notice(data["title"],data["content"]):
        return {"message":"Notice created"},201
    
@app.route("/notices",methods=["GET"])
def api_view_all_notice():
    notices=get_all_notice()
    return jsonify([
        {
            "id":notice.id,
            "title":notice.title,
            "content":notice.content,
            "created_at":notice.created_at
        }
    for notice in notices
    ])

@app.route("/notices/<int:id>",methods=["GET"])
def api_get_notice_by_id(id):
    notice=get_notice_by_id(id)
    if notice:
        return jsonify({
            "id":notice.id,
            "title":notice.title,
            "content":notice.content,
            "created_at":notice.created_at
        }),200

@app.route("/notices/<int:notice_id>",methods=["DELETE"])
def api_del_notice(notice_id):
    if remove_notice(notice_id):
        return {"message":"Notice deleted."},200
    
#TIMETABLE ROUTES

from services.timetable_service import(add_slot,
                               get_all_slots_ser,
                               get_slot,
                               remove_slot,
                               get_slots_by_day)
@app.route("/timetable",methods=["POST"])
def api_new_slot():
    data=request.get_json()
    if not isinstance(data["course_id"],int):
        return {"error":"course_id must be integer"},400
    if not data["day"]:
        return {"error":"day required"},400
    if not data["start_time"]:
        return {"error":"start_time required"},400
    if not data["end_time"]:
        return {"error":"end_time required"},400
    if not data["room"]:
        return {"error":"room_id required"},400
    if add_slot(data["course_id"],data["day"],data["start_time"],data["end_time"],data["room"]):
        return {"message":"Slot created"},201
    
@app.route("/timetable",methods=["GET"])   
def api_get_all_slot():
    slots=get_all_slots_ser()
    if slots:
        return jsonify([{
            "id":slot.id,
            "course_id":slot.course_id,
            "day":slot.day,
            "start_time":slot.start_time,
            "end_time":slot.end_time,
            "room":slot.room
        }for slot in slots]),200

@app.route("/timetable/<int:course_id>/slots",methods=["GET"])
def api_get_slots_by_cou_id(course_id):
    slots=get_slot(course_id)
    if slots:
        return jsonify([{
            "id":slot.id,
            "course_id":slot.course_id,
            "day":slot.day,
            "start_time":slot.start_time,
            "end_time":slot.end_time,
            "room":slot.room            
        }
        for slot in slots]),200
    
@app.route("/timetable/<int:id>",methods=["DELETE"])
def api_del_slot(id):
    dell=remove_slot(id)
    if dell:
        return {"message":f"{dell} deleted"},200
    
@app.route("/timetable/day/<day>",methods=["GET"])
def api_get_slots_by_day(day):
    slots=get_slots_by_day(day)
    if slots:
        return jsonify([{
        "id":slot.id,
        "course_id":slot.course_id,
        "day":slot.day,
        "start_time":slot.start_time,
        "end_time":slot.end_time,
        "room":slot.room    
        }for slot in slots])

if __name__ == "__main__":
    app.run(debug=True)

