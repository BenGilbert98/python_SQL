# pyodbc task
Task:
- Create a new file and a class with function to establish connection with pyodbc
- create a function that create a table in the DB
- create a function that prompts user to input data in that table
- create a new file called PYODBC_TASK.md and document the steps to implement the task

## Solution
### Importing pyodbc
- First pyodbc is imported as we are going to be querying an SQL database
``` python
import pyodbc
```
### Defining the class
- Then, a class is defined and initialised with server, database, username, password and driver.
``` python
class Db_connect:
    def __init__(self):
        self.server = 'databases1.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = '************'
        self.password = '*********'
        self.driver = '{ODBC Driver 17 for SQL Server}'
```
### Create_table Method
- A create_table method is created
- connection and cursor are established using the following code:
```python
def create_table(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
```
- The SQL query is defined using
``` python
cursor.execute('''

               CREATE TABLE bens_table
               (
               column1 VARCHAR(255),
               column2 VARCHAR(255),
               column3 VARCHAR(255)
               )

               ''')
```
- The changes are committed to the database using
``` python
        connect.commit()
```
### input_data Method
- A method is defined to insert user inputted data into the database
- Similarly to our create_table method, connection and cursor are established
- a,b and c take input from the users and store them within their respective variable
- execute statement inserts a,b and c into column 1,2 and 3 respectively
- The change is then committed to the database
``` python
    def input_data(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        a = input("column 1 value -->    ")
        b = input("column 2 value -->    ")
        c = input("column 3 value -->    ")
        cursor.execute(f" INSERT INTO bens_table (column1, column2, column3) VALUES ('{a}','{b}','{c}');")
        connect.commit()
```
### Query Method
- A method is defined to display the data from our newly created and manipulated table
- Similarly to our create_table method, connection and cursor are established
- execute statement will select all values from the table
- The data is then printed within python
``` python
    def query(self):
        connect = pyodbc.connect(
            'DRIVER=' + self.driver + ';SERVER=' + self.server + ';PORT=1433;DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        cursor = connect.cursor()
        result = cursor.execute("SELECT * FROM bens_table").fetchall()
        print(result)
```