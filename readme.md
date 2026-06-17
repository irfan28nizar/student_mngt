# Campus Utility Backend System

## Overview

Campus Utility Backend System is a RESTful backend application built using Python, Flask, and SQLite.

The project provides APIs for managing:

* Students
* Courses
* Notices
* Timetable Slots
* Administrator Authentication

The application follows a layered architecture consisting of API Layer, Service Layer, and Database Layer to maintain separation of concerns and improve maintainability.

⸻

## Features

### Student Management

* Create Student
* View All Students
* View Student by ID
* Update Student Semester
* Delete Student
* Department Filtering
* Semester Filtering
* Pagination

### Course Management

* Create Course
* View All Courses
* View Course by ID
* Delete Course
* Duplicate Course Detection
* Credit Validation

### Notice Management

* Create Notice
* View All Notices
* View Notice by ID
* Soft Delete Notice
* Restore Deleted Notice

### Timetable Management

* Create Timetable Slot
* View All Slots
* View Slots by Course
* View Slots by Day
* Delete Slot
* Room Conflict Detection
* Time Conflict Validation
* Pagination
* Filtering

### Authentication

* Admin Registration
* Password Hashing
* Login Verification
* Password Policy Validation

### Security

* SQL Injection Prevention
* Parameterized Queries
* Input Validation
* Input Sanitization
* Defensive Programming
* Pagination Abuse Prevention

⸻

## Architecture

``` layers
Client
↓
API Layer (Flask Routes)
↓
Service Layer (Business Logic)
↓
Database Layer (SQLite Queries)
↓
SQLite Database
```

### API Layer

Responsible for:

* Handling HTTP Requests
* Parsing JSON Data
* Returning HTTP Responses

### Service Layer

Responsible for:

* Business Logic
* Validation Rules
* Security Checks
* Timetable Conflict Detection
* Authentication Logic

### Database Layer

Responsible for:

* Database Access
* SQL Queries
* Data Retrieval
* Data Persistence

⸻

## Tech Stack

### Backend

* Python
* Flask

### Database

* SQLite

### API Testing

* Postman

### Concepts Implemented

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

## API Documentation

### Student APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /students | Get all students |
| POST | /students | Create student |
| GET | /students/<student_id> | Get student by ID |
| PATCH | /students/<student_id> | Update student semester |
| DELETE | /students/<student_id> | Delete student |

Filtering and Pagination:
```http
GET /students?department=CSE&semester=5&page=1&page_size=10
```
⸻

### Course APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /courses | Get all courses |
| POST | /courses | Create course |
| GET | /courses/<course_id> | Get course by ID |
| DELETE | /courses/<course_id> | Delete course |

⸻

### Authentication APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register admin |
| POST | /login | Admin login |

⸻

### Notice APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /notices | Get all notices |
| POST | /notices | Create notice |
| GET | /notices/<notice_id> | Get notice by ID |
| PATCH | /notices/<notice_id> | Update notice |
| PATCH | /notices/<notice_id>/restore | Restore deleted notice |

⸻

### Timetable APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /timetable | Get all timetable slots |
| POST | /timetable | Create timetable slot |
| GET | /timetable/<course_id>/slots | Get slots by course ID |
| GET | /timetable/day/<day> | Get slots by day |
| DELETE | /timetable/<slot_id> | Delete timetable slot |

Filtering and Pagination:

```http
GET /timetable?course_id=1&day=Monday&room=A101&page=1&page_size=10
```
⸻

Timetable Conflict Detection

The system prevents overlapping timetable slots in the same room.

Conflict Logic:

```python
new_start_time < existing_end_time and
new_end_time > existing_start_time
```
If the condition evaluates to true, the slot is rejected.

⸻

## Security Measures

* Password Hashing using bcrypt
* SQL Injection Prevention using Parameterized Queries
* Input Validation
* Input Sanitization
* Defensive Programming
* Custom Exception Handling

⸻

## Future Improvements

* PostgreSQL Migration
* JWT Authentication
* Role-Based Authorization
* Automated Testing
* API Documentation using Swagger/OpenAPI

⸻

## Author

Muhammed Irfan Nizarudeen

B.Tech Computer Science Engineering

Python Backend Developer