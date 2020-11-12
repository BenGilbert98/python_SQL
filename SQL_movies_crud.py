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


def add_movie():
    titleType = input("What type of movie is it?    ")
    primaryTitle = input("What is the primary title?    ")
    originalTitle = input("What is the original title?    ")
    isAdult = input("is the move rated 18+?  (1 for yes, 0 for no)   ")
    startYear = input("What is the start year?    ")
    endYear = input("What is the end year?    ")
    runtimeMinutes = input("What is the movies runtime (minutes)?    ")
    genres = input("What genre is the movie?    ")

    cursor.execute(f"""
       INSERT INTO imdb_movies (titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
       VALUES ({titleType}, {primaryTitle}, {originalTitle}, {isAdult}, {startYear}, {endYear}, {runtimeMinutes}, {genres})
       """)

    conn.commit()


def remove_movie():
    movie = input("What is the primary title of the movie you want to remove?   ")
    cursor.execute(f"""
           DELETE FROM imdb_movies WHERE primaryTitle = {movie}
           """)
    conn.commit()