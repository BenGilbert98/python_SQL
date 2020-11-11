# This lesson will include the connection to our SQL DB from Python using pyodbc

# pyodbc helps us connect to SQL instance
import pyodbc
import pandas as pd

# we will connect to Northwind DB used in SQL week

# This is the command needed to connect to a SQL server (with pandas and pyodbc)
#
#
#
# server = 'databases1.spartaglobal.academy'
# database = 'Northwind'
# username = 'SA'
# password = 'Passw0rd2018'
# driver = '{ODBC Driver 17 for SQL Server}'
#
# # connection = pyodbc.connect (server information, username, password)
# conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = conn.cursor()
#
# sql_query = pd.read_sql_query('''
#                 SELECT TOP 5 * FROM dbo.Orders
#                 WHERE ShipCountry = 'France'
#                 ''', conn)
# print(sql_query)
# print(type(sql_query))



# These are the commands needed to connect to a SQL server (with pyodbc)
#
#
#
# This code is used to make a connection with the sql server
server = 'databases1.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()
# This is the statement which you want executed
cursor.execute('''
               SELECT TOP 5 * FROM dbo.Orders
               ''')
# This is the information you want displayed
row = cursor.fetchone()
while row:
    # prints the columns within the range specified below
    print (str(row[0]) + " " + str(row[3]))
    row = cursor.fetchone()


