from flask import Flask, jsonify , request
from services.student_service import update_student_semester, get_student_by_id,get_all_students,add_student
app=Flask(__name__)
@app.route("/")
def home():
    return{"message":"Backend Working"}

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
    if not data["semester"].strip():
        return {"error":"Semester is required"},400
    add_student(data["name"],data["department"],data["semester"])
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
    else:
        return {"error":"Student not found"},404

@app.route("/students/<int:student_id>",methods=["PATCH"])
def update_student_by_semester(student_id):
    data=request.get_json()
    if "semester" not in data:
        return {"error":"Semester is required"},400
    if not isinstance(data["semester"],int):
        return {"error":"Semester must be an integer"},400
    
    if update_student_semester(data["semester"],student_id):
        return {"message":"Student semester updated"},200
    else:
        return {"error":"Failed to update student semester"},404

if __name__ == "__main__":
    app.run(debug=True)

