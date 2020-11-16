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

### Functions

#### Delete
- A delete function was made in which you can delete the table created from the csv file.
``` python
def delete():
    cursor.execute(
        'DELETE FROM imdb_movies_ben')
```

#### Create
- Create function created which creates a table inside Northwind with the corresponding column names.
``` python
def create():
    cursor.execute(
        'CREATE TABLE imdb_movies_ben (titleType VARCHAR(255), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear nvarchar(255), runtimeMinutes nvarchar(255), genres nvarchar(255))')
```

#### Insert_csv_data
- This function is responsible for inserting the csv file data into the newly created table.
``` python
def insert_csv_data():
    for row in df.itertuples():
        cursor.execute("""
            INSERT INTO imdb_movies_ben (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
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

#### Insert Data
- This function will take user inputs for each column name and insert it into the table created above.
- Commit is used to push the changes to the database
``` python
def insert_data():
    titleType = input("what is the title type for the movie?    ")
    primaryTitle = input("what is the primary title type for the movie?    ")
    originalTitle = input("what is the original title type for the movie?    ")
    isAdult = "0"
    startYear = input("What is the start year?    ")
    endYear = input("What is the end year?    ")
    runtimeMinutes = input("What is the runtime of the movie (minutes)?    ")
    genres = input("What genre is the movie?    ")
    cursor.execute(f"""INSERT INTO imdb_movies_ben 
                        (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
                VALUES 
                        ('{titleType}', '{primaryTitle}', '{originalTitle}', '{isAdult}', '{startYear}', '{endYear}', '{runtimeMinutes}', '{genres}')
                """)
    conn.commit()
```

#### SQL Query
- This function will take an SQL query statement from the user and execute it.
- The result is then displayed to the user.
``` python
def sql_query():
    query = input("Please enter your sql query    ")
    exported_data = pd.read_sql_query(f'{query}', conn)
    df_2 = pd.DataFrame(exported_data)
    print(df_2)
```

#### SQL to CSV
- This function will take an sql query and desired file name, execute and display the data and then save it within a csv file.
``` python
def sql_to_csv():
    query = input("Please enter your sql query    ")
    file_name = input("Please enter a file name    ")
    exported_data = pd.read_sql_query(f'{query}', conn)
    df_2 = pd.DataFrame(exported_data)
    print(df_2)
    df_2.to_csv(fr'C:\Users\bengi\PycharmProjects\python_SQL\{file_name}.csv')
```

#### UI
- This function displays the options available to the user and takes input to determine which function to carry out.
- While loop is used to keep prompting the user until "exit" is typed
``` python
def UI():
    options = ['create table from csv file', 'insert csv file data', 'insert data into database', 'sql query', 'delete', 'sql to csv']
    while True:
        user_input = input(f"Which method would you like to use? \n {options} \n type exit to leave. \n ")
        if user_input == "delete":
            delete()
        if user_input == "create table from csv file":
            create()
        if user_input == "insert csv file data":
            insert_csv_data()
        if user_input == "sql query":
            sql_query()
        if user_input == "sql to csv":
            sql_to_csv()
        if user_input == "insert data into database":
            insert_data()
        elif user_input == "exit":
            break
```
