from database import create_tables
from services.student_service import (add_student,
                                      delete_student,
                                      get_all_students,
                                      get_student_by_department,
                                      get_students_by_semester,
                                      update_student,
                                      get_students_by_department_and_semester
                                      )
from services.course_service import(add_course,
                                  delete_course,
                                  get_all_courses)

def show_menu_student():
    print("\nStudent Management System")
    print("\n1.Add Student")
    print("2.Update Student")
    print("3.Delete Student")
    print("4.View All Students")
    print("5.View Students by Department")
    print("6.Filter students by semester")
    print("7.Search students by department and semester")
    print("8.Exit")

def show_menu_course():
    print("\nCourse Management System")
    print("\n1.Add Course")
    print("2.View All Courses")
    print("3.Delete Course")
    print("4.Exit")

def show_menu():
    print("\nMain Menu")
    print("\n1.Student Management")
    print("2.Course Management")
    print("3.Exit")

def main():
    create_tables()

    while True:
        show_menu()
        choice=input("\nEnter your choice: ")

        if choice=="1":
            while True:
                show_menu_student()
                student_choice=input("\nEnter your choice: ")



                if student_choice=="1":
                    print("\nAdd New Student")
                    name=input("Enter the student name:").strip()
                    department=input("Enter the student department:").strip()
                    try:
                        semester=int(input("Enter the semester:"))
                    except ValueError :
                        print("Semester must be an integer value.")
                        continue
                    student=add_student(name,department,semester)
                    print(f"\n Student added succesfully \n {student}.")



                elif student_choice=="2":
                    print("\n Update student")
                    try:
                        student_id=int(input("Enter Student ID to update:"))
                        name=input("Enter the new name:").strip()
                        department=input("Enter the new department:").strip()
                        semester=int(input("Enter the new semester:"))
                    except ValueError:
                        print("Student ID must be integer value.")
                        continue
                    val=update_student(student_id,name,department,semester)
                    if not val:
                        print(f"\nNo student found  with ID {student_id}.")
                    else:
                        print(f"\nStudent with ID {student_id} updated successfully.")



                elif student_choice=="3":
                    print("\nDelete Student Selected")
                    try:
                        student_id=int(input("Enter Student ID to delete:"))

                    except ValueError:
                        print("Student ID must be an integer.")
                        continue
                    r=delete_student(student_id)
                    if not r:
                        print(f"\nNo student found with ID {student_id}.")
                    else:
                        print(f"\nStudent with ID {student_id} deleted successfully.")
                    

                elif student_choice=="4":
                    print("\n View All Students")
                    students=get_all_students()
                    if not students:
                        print("\n No students found.")
                    else:
                        for s in students:
                            print(s)


                elif student_choice=="5":
                    print("\nView Students by Department")
                    department=input("Enter the department name:")
                    students=get_student_by_department(department)
                    if not students:
                        print(f"\nNo students found in department {department}.")
                    else:
                        for s in students:
                            print(s)



                elif student_choice=="6":
                    print("\nFilter students by semester")
                    try:
                        semester=int(input("Enter the semester:"))
                    except ValueError:
                        print("Semester must be an integer.")
                        continue
                    students=get_students_by_semester(semester)
                    if not students:
                        print(f"\nNo students found in semester {semester}.")
                    else:
                        for s in students:
                            print(s) 



                elif student_choice=="7":
                    print("\nSearch Students By Department and Semester")
                    dept=input("Enter the department name(leave empty to skip):").strip()
                    sem=input("Enter the semester(leave empty to skip):").strip()
                    try:
                        semes=int(sem) if sem else None
                    except ValueError:
                        print("Semester must be an integer.")
                        continue
                    students=get_students_by_department_and_semester(department=dept if dept else None,semester=semes)
                    if not students:
                        print("\nNo students found matching the criteria.")
                    else:
                        for s in students:
                            print(s)



                elif student_choice=="8":
                    print("\nExiting Student Management Menu. Returning to Main Menu.")
                    break
                else:
                    print("\nInvalid choice. Please try again.")




        elif choice=="2":
            while True:
                show_menu_course()
                course_choice=input("\nEnter your choice:")

                if course_choice=="1":
                    print("\nAdd New Course")
                    name=input("Enter name of the course:")
                    try:
                        credits=int(input ("enter the credits for the course:"))
                    except ValueError:
                        print("Credits must be integer value.")
                        continue
                    course=add_course(name,credits)
                    if not course:
                        print("\nFailed to add course.")
                    else:
                        print(f"\nCourse added successfully:\n{course}")


                elif course_choice=="2":
                    print("\nView All Courses")
                    courses=get_all_courses()
                    if not courses:
                        print("\nNo courses found.")
                    else:
                        for c in courses:
                            print(c)



                elif course_choice=="3":
                    print("\nDelete Course")
                    try:
                        course_id=int(input("Enter the course ID:"))
                    except ValueError:
                        print("Course ID must be an integer.")
                        continue
                    course=delete_course(course_id)
                    if not course:
                        print(f"\nNo course found with ID {course_id}.")
                    else:
                        print(f"\nCourse with ID {course_id} deleted successfully.")

                elif course_choice=="4":
                    print("\nExiting Course Management Menu. Returning to Main Menu.")
                    break
                else:
                    print("\nInvalid choice. Please try again.")



        elif choice=="3":
            print("\nExiting the Main Menu. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
    
if __name__ == "__main__":
    main()