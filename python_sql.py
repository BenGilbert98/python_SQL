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

# sql_query = pd.read_sql_query('''
#                 SELECT TOP 5 * FROM [Order Details]
#                 ORDER BY Quantity DESC
#                 ''', conn)
# print(sql_query)
# print(type(sql_query))


# These are the commands needed to connect to a SQL server (with pyodbc)
#
#
#
# This code is used to make a connection with the sql server
# server = 'databases1.spartaglobal.academy'
# database = 'Northwind'
# username = '******'
# password = '**********'
# driver = '{ODBC Driver 17 for SQL Server}'
#
# conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# # cursor is location of your mouse / current path
#
# cursor = conn.cursor()
# # This is the statement which you want executed
# cursor.execute('''
#                SELECT TOP 5 * FROM [Order Details]
#                ''')
# This is the information you want displayed
# row = cursor.fetchone()

# while row:
#     # prints the columns within the range specified below
#     print (str(row[2]) + " " + str(row[4]))
#     row = cursor.fetchone()


server = 'databases1.spartaglobal.academy'
database = 'Northwind'
username = '****'
password = '********'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()
cust_row = cursor.execute('''
               SELECT * FROM Customers;
               ''').fetchall()
                    # using fetchall allows us to get all the data inside customers table
for records in cust_row:
    print(records)

# There is another table in the DB called Products

product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Running queries in our python program to access database
for product_records in product_rows:
    # iterate through the table data and find the unit prices
    print(product_records.UnitPrice)


# product table data
product_row = cursor.execute("SELECT * FROM Products")

# iterating through until the last line of the data (until condition is False)(Until data is not available)
while True:
    records = product_row.fetchone()
    if records is None:
        break
    else:
        print(records.UnitPrice)
