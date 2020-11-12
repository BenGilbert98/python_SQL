import pyodbc
import pandas as pd

data = pd.read_csv(r'C:\Users\bengi\PycharmProjects\python_SQL\imdbtitles.csv')
df = pd.DataFrame(data, columns=['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear',
                                 'runtimeMinutes', 'genres'])
# print(df)

server = 'databases1.spartaglobal.academy'
database = 'Northwind'
username = '********'
password = '***'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

cursor.execute(
    'CREATE TABLE imdb_movies (titleType VARCHAR(255), primaryTitle VARCHAR(255), originalTitle VARCHAR(255), isAdult INT, startYear INT, endYear nvarchar(255), runtimeMinutes nvarchar(255), genres nvarchar(255))')

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

sql_query = pd.read_sql_query('SELECT * FROM imdb_movies', conn)
print(sql_query)

exported_data = pd.read_sql_query('''SELECT * FROM imdb_movies''', conn)
df_2 = pd.DataFrame(exported_data)
df.to_csv(r'C:\Users\bengi\PycharmProjects\python_SQL\imdbtitlesfromsql.csv')
