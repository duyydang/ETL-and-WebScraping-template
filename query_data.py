import sqlite3
import pandas as pd

db_name = 'Data/Banks.db'
table_name = 'Largest_banks'

conn = sqlite3.connect(db_name)

query_all = pd.read_sql('SELECT * FROM Largest_banks', conn)
print(query_all)

query_AVG_London = pd.read_sql(
    'SELECT AVG(MC_GBP_Billion) from '+table_name, conn)
print(query_AVG_London)

query_limit_London = pd.read_sql(
    'SELECT Name from Largest_banks LIMIT 5', conn)
print(query_limit_London)

# query_London = pd.read_sql('SELECT Name,MC_GBP_Billion from '+table_name, conn)
# print(query_London)
# print()

# query_Berlin = pd.read_sql('SELECT Name,MC_EUR_Billion from '+table_name, conn)
# print(query_Berlin)
# print()

# query_New_Delhi = pd.read_sql(
#     'SELECT Name,MC_INR_Billion from '+table_name, conn)
# print(query_New_Delhi)
# print()
