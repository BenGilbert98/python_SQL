SQL OOP

    OOP task using pyodbc

An sql manager for the products table

create an object that relates only to the products table in the Northwind database. The reason for creating a single object for any table within the database would be to ensure that all functionality we build into this relates to what could be defined as a 'business function'.

As an example the products table, although relating to the rest of the company, will service a particular area of the business in this scenario we will simply call them the 'stock' department.

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions within a single object.

Create two files nw_products.py & nw_runner.py and then we will move into creating our object.

Our first requirement...
We've had a requirement for the stock department to print out the average value of all of our stock items.

Away we go....

!!!Important Note!!! It would be more efficient to write the SQL query to find the data and compute the value and simply return the value in Python. 

## Solution
- The main file (nw_runner) is created
- An instance of the Query class is created with argument "Products"
- The functions query and stock are called
``` python
from nw_products import Query

products = Query("Products")
products.query()
products.stock()
```


- The first step is to import pyodbc as we will be querying a database
- Next, a class is defined with attributes of servxer, database, username, password, driver and table_name
``` python
class Query:
    def __init__(self, table_name):
        self.server = 'databases1.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.driver = '{ODBC Driver 17 for SQL Server}'
        self.table_name = table_name
```
- A method to find the average unit price is established:
```
  def query(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute(f'''

                       SELECT AVG(UnitPrice) FROM {self.table_name}

                       ''').fetchone()
        for i in result:
            print(i)
```
- The code below is responsible for connecting to the database using the attributes and executing a query which is defined in the cursor.execute statement
``` python
 connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute(f'''

                       SELECT AVG(UnitPrice) FROM {self.table_name}

                       ''').fetchone()
```
- Then, a method is defined to find the value of the remaining stock which is equal to the unitprice * products in stock
- A for loop is used to iterate through the result and print it in a more user friendly format.
``` python
    def stock(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute(f'''

                               SELECT ProductName, CONVERT(DECIMAL(10,2),UnitsInStock * UnitPrice) FROM {self.table_name}

                               ''').fetchall()
        for i, j in result:
            print(i, ":", j)
```

- Together:
```python
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

                       SELECT AVG(UnitPrice) FROM {self.table_name}

                       ''').fetchone()
        for i in result:
            print(i)

    def stock(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute(f'''

                               SELECT ProductName, CONVERT(DECIMAL(10,2),UnitsInStock * UnitPrice) FROM {self.table_name}

                               ''').fetchall()
        for i, j in result:
            print(i, ":", j)
```