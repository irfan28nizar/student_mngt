#Campus Utility Backend System

##Overview

Campus Utility Backend System is a RESTful backend application built using Python, Flask, and SQLite.

The project provides APIs for managing:

* Students
* Courses
* Notices
* Timetable Slots
* Administrator Authentication

The application follows a layered architecture consisting of API Layer, Service Layer, and Database Layer to maintain separation of concerns and improve maintainability.

⸻

##Features

###Student Management

* Create Student
* View All Students
* View Student by ID
* Update Student Semester
* Delete Student
* Department Filtering
* Semester Filtering
* Pagination

###Course Management

* Create Course
* View All Courses
* View Course by ID
* Delete Course
* Duplicate Course Detection
* Credit Validation

###Notice Management

* Create Notice
* View All Notices
* View Notice by ID
* Soft Delete Notice
* Restore Deleted Notice

###Timetable Management

* Create Timetable Slot
* View All Slots
* View Slots by Course
* View Slots by Day
* Delete Slot
* Room Conflict Detection
* Time Conflict Validation
* Pagination
* Filtering

###Authentication

* Admin Registration
* Password Hashing
* Login Verification
* Password Policy Validation

###Security

* SQL Injection Prevention
* Parameterized Queries
* Input Validation
* Input Sanitization
* Defensive Programming
* Pagination Abuse Prevention

⸻

##Architecture

Client
↓
API Layer (Flask Routes)
↓
Service Layer (Business Logic)
↓
Database Layer (SQLite Queries)
↓
SQLite Database

###API Layer

Responsible for:

* Handling HTTP Requests
* Parsing JSON Data
* Returning HTTP Responses

###Service Layer

Responsible for:

* Business Logic
* Validation Rules
* Security Checks
* Timetable Conflict Detection
* Authentication Logic

###Database Layer

Responsible for:

* Database Access
* SQL Queries
* Data Retrieval
* Data Persistence

⸻

##Tech Stack

###Backend

* Python
* Flask

###Database

* SQLite

###API Testing

* Postman

###Concepts Implemented

* REST APIs
* Layered Architecture
* CRUD Operations
* Authentication
* Pagination
* Filtering
* Soft Delete
* Validation
* Exception Handling
* SQL Injection Prevention

⸻

##API Documentation

Student APIs

Method	Endpoint	             Description
GET	    /students	            Get all students
POST	/students	            Create student
GET	    /students/<student_id>	Get student by ID
PATCH	/students/<student_id>	Update student semester
DELETE	/students/<student_id>	Delete student

Filtering and Pagination:

GET /students?department=CSE&semester=5&page=1&page_size=10

⸻

###Course APIs

Method	    Endpoint
GET 	    /courses
POST        /courses
GET	        /courses/<course_id>
DELETE	    /courses/<course_id>

⸻

###Authentication APIs

Method	Endpoint
POST	/register
POST	/login

⸻

###Notice APIs

Method	Endpoint
GET	    /notices
POST	/notices
GET	    /notices/<notice_id>
PATCH	/notices/<notice_id>
PATCH	/notices/<notice_id>/restore

⸻

###Timetable APIs

Method	Endpoint
GET	    /timetable
POST	/timetable
GET	    /timetable/<course_id>/slots
GET	    /timetable/day/<day>
DELETE	/timetable/<slot_id>

Filtering and Pagination:

GET /timetable?course_id=1&day=Monday&room=A101&page=1&page_size=10

⸻

Timetable Conflict Detection

The system prevents overlapping timetable slots in the same room.

Conflict Logic:

new_start_time < existing_end_time

AND

new_end_time > existing_start_time

If the condition evaluates to true, the slot is rejected.

⸻

##Security Measures

* Password Hashing using bcrypt
* SQL Injection Prevention using Parameterized Queries
* Input Validation
* Input Sanitization
* Defensive Programming
* Custom Exception Handling

⸻

##Future Improvements

* PostgreSQL Migration
* JWT Authentication
* Role-Based Authorization
* Automated Testing
* API Documentation using Swagger/OpenAPI

⸻

Author

Muhammed Irfan Nizarudeen

B.Tech Computer Science Engineering

Python Backend Developer