import pyodbc


class Query:
    def __init__(self, table_name):
        self.server = 'databases1.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.table_name = table_name

    def query(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute(f'''

                       SELECT AVG(UnitPrice) AS "Average Unit Price" FROM {self.table_name}

                       ''').fetchall()
        for i in result:
            print(i)