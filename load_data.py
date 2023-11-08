import sqlite3

csv_path = 'Data/Largest_banks_data.csv'
db_name = 'Data/Banks.db'
table_name = 'Largest_banks'


def load_to_csv(df):
    df.to_csv(csv_path)


def load_to_db(df):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()


def load_all(df):
    load_to_csv(df)
    load_to_db(df)
