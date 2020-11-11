import pyodbc


class Query:
    def __init__(self):
        self.server = 'databases1.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.driver = '{ODBC Driver 17 for SQL Server}'
