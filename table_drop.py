
# Quick Table Create

import sqlite3


data_base = "book_database"
#===Connect database to python===
db = sqlite3.connect(f'data/{data_base}')
cursor = db.cursor()

#===This command is here for the purpose of deleting the entire table, so all the commands can be seen in action===
TABLE_PARAMETER = "TABLE_PARAMETER"
DROP_TABLE_SQL = f"DROP TABLE {TABLE_PARAMETER};"
GET_TABLES_SQL = "SELECT name FROM sqlite_schema WHERE type='table';"


def delete_all_tables(db):
    tables = get_tables(db)
    delete_tables(db, tables)


def get_tables(db):
    cursor.execute(GET_TABLES_SQL)
    tables = cursor.fetchall()
    return tables


def delete_tables(db, tables):
    for table, in tables:
        sql = DROP_TABLE_SQL.replace(TABLE_PARAMETER, table)
        cursor.execute(sql)

delete_all_tables(data_base)

cursor.close()
db.close()