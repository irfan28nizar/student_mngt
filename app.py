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
def view_students():
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
def create_student():
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
def get_student(student_id):
    student=get_student_by_id(student_id)
    if student:
        return jsonify({
            "id":student.student_id,
            "name":student.name,
            "department":student.department,
            "semester":student.semester
        }),200

@app.route("/students/<int:student_id>",methods=["PATCH"])
def update_student_by_semester(student_id):
    data=request.get_json()
    if "semester" not in data:
        return {"error":"Semester is required"},400
    if not isinstance(data["semester"],int):
        return {"error":"Semester must be an integer"},400
    
    if update_student(data["semester"],student_id):
        return {"message":"Student semester updated"},200
    else:
        return {"error":"Failed to update student semester"},404
    
#ADMIN ROUTES

@app.route("/register",methods=["POST"])
def register():
    data=request.get_json()
    if not data["username"].strip():
        return{"error":"Username is required"},400
    if not data["password"].strip():
        return{"error":"Password is required"},400
    if not checkpass(data["password"]):
        return{"error":"Password must be at least 8 characters long, contain a number, an uppercase letter, a lowercase letter, and a special character"},400
    admin=register_admin(data["username"],data["password"])
    return {"message":"Admin registered successfully"},201

@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    if not data["username"].strip():
        return{"error":"Username is required"},400
    if not data["password"].strip():
        return{"error":"Password is required"},400
    if login_admin(data["username"],data["password"]):
        return{"message":"Login Successful"},200





if __name__ == "__main__":
    app.run(debug=True)

