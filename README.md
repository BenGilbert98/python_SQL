# Python SQL
![](images/Python_sql.png)
## Pyodbc (Python Open Database Connectivity)
- Allows us to connect to SQL from python program
### Setting up pyodbc
- install relevant pyodbc drivers for your OS ```https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15```
- Command to install pyodbc ``` pip install pyodbc ```
- create python_sql.py file
- Set up a pyodbc connection
- Establish connection using the following code:
```python
import pyodbc

server = 'databases1.spartaglobal.academy'
database = 'Northwind'
username = '****'
password = '*******'
driver = '{ODBC Driver 17 for SQL Server}'

# connection = pyodbc.connect (server information, username, password)
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

```
- Make a query
```python
cursor.execute('''
               SELECT TOP 5 * FROM dbo.Orders
               ''')
# This is the information you want displayed
row = cursor.fetchone()
print(row)

```

### Cursor in Python and how to use it
- create a variable for cursor 
```python
cursor = conn.cursor()
```
- ```cursor.execute(" ")``` is used to query the SQL server                                     
```
cursor.execute('''
               <Execute Statement>
               ''')
```
### Functions to interact with SQL data
##### Example 1 
```python
product_rows = cursor.execute("SELECT * FROM Products").fetchall()
# Running queries in our python program to access database
for product_records in product_rows:
    # iterate through the table data and find the unit prices
    print(product_records.UnitPrice)

```
##### Example 2
```python
while True:
    records = product_row.fetchone()
    if records is None:
        break
    else:
        print(records.UnitPrice)
```

##### Example 3
```python
cust_row = cursor.execute('''
               SELECT * FROM Customers;
               ''').fetchall()
                    # using fetchall allows us to get all the data inside customers table
for records in cust_row:
    print(records)
```

## Summary
- pyodbc installation and connection set up
- cursor utilisation
- fetchone() - select each record
- fetchall() - select all records

## Task
- Create a new file and a class with functions to establish connection with pyodbc 