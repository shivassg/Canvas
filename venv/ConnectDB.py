import mysql.connector
from mysql.connector import Error

class ConnectDB:

    def __init__(self):
        self.connection = mysql.connector.connect(host='localhost',database='Canvas',user='root', password='shiva123')
        try:
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                #print("Connected to MySQL database... MySQL Server version on ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)
        self.cursor = self.connection.cursor()

    def execute(self,query, params):
        self.cursor.execute(query,params)
        self.connection.commit()


    def query(self, sql, params= None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()






