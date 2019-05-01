from ConnectDB import *
import mysql.connector
from Courses import *

class Users():

    def addUser(self):
        try:
            conn = ConnectDB()
            query = "insert into `Users` (`UserID`,`Fname`,`Lname`,`Email`,`PhoneNum`, `UserType`) " \
                    "VALUES (%s,%s,%s,%s,%s,%s)"

            params = ('1056088','Shiva','Ganesan','sganesan@gmail.com','203','Professor')
            conn.query(query,params)
            print("Successfully added Courses")
        except mysql.connector.IntegrityError as err:
            print("Error: {}".format(err))

def main():
    user = Users()
    user.addUser()
    courses = Courses()
    courses.addCourse()
    courses.addStudent()


if __name__ == "__main__":
    main()