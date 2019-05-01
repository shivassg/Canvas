from ConnectDB import *
import mysql.connector

class Courses():


    def addCourse(self):
        try:
            conn = ConnectDB()
            query = "insert into `Courses` (`CourseID`,`CourseName`,`Semester`,`Department`,`ProfessorID`,`CourseLevel`) " \
                    "VALUES (%s,%s,%s,%s,%s,%s)"

            params = ('102','Python','Fall2019','ComputerScience','101','Graduate')
            conn.query(query,params)
            print("Successfully added course")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

    def addStudent(self):
        try:
            conn = ConnectDB()
            query = "insert into `course_student_table` (`CourseID`,`StudentID`,`Semester`) " \
                    "VALUES (%s,%s,%s)"

            params = ('101','101','Fall2019')
            conn.query(query, params)
            print("Successfully added student to Course")

        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))
