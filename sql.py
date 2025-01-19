import pyodbc
import pandas as pd

connection_string = ("Driver={ODBC Driver 17 for SQL Server};"

                     "N-5CG1232HV3\MSSQLSERVER01"

                     "Database=adventureworks;"

                     "Trusted_Connection=yes;")

Connection = pyodbc.connect(connection_string)
Cursor = Connection.cursor()
df = pd.read_sql('select  * from SalesLT.Customer', Connection)
print(df)
