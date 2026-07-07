import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

cur = conn.cursor()

cur.execute("""select * from data""")
table_names = cur.fetchall()
print(table_names)

conn.close()

conn = sqlite3.connect('data.sqlite')

df= pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table'", conn) 
type(df)
pd.core.frame.DataFrame
pd.read_sql("SELECT * FROM offices", conn)
conn.close()

