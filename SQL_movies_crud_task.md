SQL Movies CRUD
Timings

60 Minutes
Summary

Now that you've learned how to connect to the DB using pyodbc you can start abstracting out interaction the db! This is great if you don't like writing sql.
Tasks

    CRUD the DB

Hint: create abstraction and methods to deal with db so you don't have too
Acceptance Criteria

    You can get all the movies
    you can search based on title

    you can add movies to DB

    second iteration:

IMDB CSV <> Py <> SQL
Summary

You know how to parse csv files into python.
You also know how to connect python into the db.
You also know how to manipulated and change data with python.

Your task is to move data from csv file into the db and from the the db into text files
Tasks

    read the text file and create object

    save object in DB

    Load that from DB and create object
    output object to text file

Extra:
* Explore other APIs
Acceptance Criteria

    able to take in 10 film names in text file and save to db
    able to load data from DB and create text file with names

## Solution
- First we have to import the relevant modules pyodbc and pandas
- ```data = pd.read_csv(r'C:\Users\beng\PycharmProjects\python_SQL\imdbtitles.csv')``` will read a specified csv file
- The next section of code is respondible for creating a dataframe with the csv file data with specified column names
- ```df = pd.DataFrame(data, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear','runtimeMinutes', 'genres'])```

```python
import pyodbc
import pandas as pd

data = pd.read_csv(r'C:\Users\beng\PycharmProjects\python_SQL\imdbtitles.csv')
df = pd.DataFrame(data, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                 'runtimeMinutes', 'genres'])
```
- Then we must establish a connection to our SQL server
``` python
server = 'databases1.spartaglobal.academy'
database = 'Northwind'
username = '***'
password = '***'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()
```
- Once connected, a table must be created inside our sql database with table name, column titles and data types specified
``` python
cursor.execute('CREATE TABLE imdb_movies (titleType VARCHAR(255), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear nvarchar(255), runtimeMinutes nvarchar(255), genres nvarchar(255))')
```
- Then, data is added to the database 
``` python
for row in df.itertuples():
    cursor.execute("""
    INSERT INTO imdb_movies (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
                   row.titleType,
                   row.primaryTitle,
                   row.originalTitle,
                   row.isAdult,
                   row.startYear,
                   row.endYear,
                   row.runtimeMinutes,
                   row.genres)

    conn.commit()
```
- Lastly, to export the data back into a new csv file.
- ```pd.read_sql_query('''SELECT * FROM imdb_movies''', conn)``` is used to read the data from an sql query
- ```df_2 = pd.DataFrame(exported_data)``` converts the queried data to a dataframe
- ```df.to_csv(r'C:\Users\beng\PycharmProjects\python_SQL\imdbtitlesfromsql.csv')``` writes the data into a csv file
``` python
exported_data = pd.read_sql_query('''SELECT * FROM imdb_movies''', conn)
df_2 = pd.DataFrame(exported_data)
df.to_csv(r'C:\Users\beng\PycharmProjects\python_SQL\imdbtitlesfromsql.csv')
```