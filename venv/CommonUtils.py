from ConnectDB import *


class CommonUtils(object):
    @staticmethod
    def getUserIDfromUserName(userNameText):
        conn = ConnectDB()
        query = "Select UserID from users where Username=%s"
        params = (userNameText,)
        userIDList = conn.query(query,params)
        userID = userIDList[0][0]
        return userID



    @staticmethod
    def getUserTypeFromUserName(userNameText):
        conn = ConnectDB()
        query = "Select UserType from users where Username=%s"
        params = (userNameText,)
        userTypeList = conn.query(query, params)
        userType = userTypeList[0][0]
        return userType

    @staticmethod
    def getFnameFromUserName(userNameText):
        conn = ConnectDB()
        fnamequery = "Select Fname from users where Username = %s"
        fnameparams = (userNameText,)
        firstNameList = conn.query(fnamequery, fnameparams)
        firstName = firstNameList[0][0]
        return firstName

    @staticmethod
    def checkLogin(userNameText, passwordText):
        isLogginValid = True
        conn = ConnectDB()
        query = "Select UserType from users where Username=%s and password=%s"
        params = (userNameText, passwordText)
        userType = conn.query(query, params)
        if not userType:
            isLogginValid = False

        return isLogginValid

    @staticmethod
    def getCourseNameFromCourseID(courseID):
        conn = ConnectDB()
        query = "Select CourseName from Courses where CourseID = %s"
        params = (courseID,)
        courseNameList = conn.query(query,params)
        courseName = courseNameList[0][0]
        return courseName


    @staticmethod
    def getCourseNumberNameYearFromCourseID(courseID):
        conn = ConnectDB()
        query = "Select CourseNumber,CourseName,Semester from Courses where CourseID = %s"
        params = (courseID,)
        courseNumberList = conn.query(query,params)
        return courseNumberList

    @staticmethod
    def getCourseIDFromNumberAndSemester(coureNumber, Semester):
        conn = ConnectDB()
        query = "Select CourseID from Courses where CourseNumber= %s and Semester= %s"
        params = (coureNumber,Semester)
        courseIDList = conn.query(query, params)
        courseID = courseIDList[0][0]
        return courseID






