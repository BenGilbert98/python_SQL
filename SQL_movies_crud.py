import pyodbc
import pandas as pd

file_location = input("Where is the csv file located? ")
data = pd.read_csv(fr'{file_location}')
df = pd.DataFrame(data, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                 'runtimeMinutes', 'genres'])
# print(df)

server = 'databases1.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()


def delete():
    cursor.execute(
        'DELETE FROM imdb_movies_ben')


def create():
    cursor.execute(
        'CREATE TABLE imdb_movies_ben (titleType VARCHAR(255), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear nvarchar(255), runtimeMinutes nvarchar(255), genres nvarchar(255))')


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

def sql_query():
    query = input("Please enter your sql query    ")
    exported_data = pd.read_sql_query(f'{query}', conn)
    df_2 = pd.DataFrame(exported_data)
    print(df_2)


def sql_to_csv():
    query = input("Please enter your sql query    ")
    file_name = input("Please enter a file name    ")
    exported_data = pd.read_sql_query(f'{query}', conn)
    df_2 = pd.DataFrame(exported_data)
    print(df_2)
    df_2.to_csv(fr'C:\Users\bengi\PycharmProjects\python_SQL\{file_name}.csv')


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


UI()
