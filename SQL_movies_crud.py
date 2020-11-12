import pyodbc
import pandas as pd

data = pd.read_csv(r'C:\Users\bengi\PycharmProjects\python_SQL\imdbtitles.csv')
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


sql_to_csv()