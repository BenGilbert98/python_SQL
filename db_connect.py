import pyodbc


class Db_connect:
    def __init__(self):
        self.server = 'databases1.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.driver = '{ODBC Driver 17 for SQL Server}'

    def create_table(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        cursor.execute('''

               CREATE TABLE bens_table
               (
               column1 VARCHAR(255),
               column2 VARCHAR(255),
               column3 VARCHAR(255)
               )

               ''')
        connect.commit()

    def input_data(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        a = input("column 1 value -->    ")
        b = input("column 2 value -->    ")
        c = input("column 3 value -->    ")
        cursor.execute(f" INSERT INTO bens_table (column1, column2, column3) VALUES ('{a}','{b}','{c}');")
        connect.commit()

    def query(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute("SELECT * FROM bens_table").fetchall()
        print(result)


table = Db_connect()
table.create_table()
table.input_data()
table.query()
