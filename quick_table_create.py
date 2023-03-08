# Quick Table Create

import sqlite3


data_base = "book_database"
#===Connect database to python===
db = sqlite3.connect(f'data/{data_base}')
cursor = db.cursor()

#===This command is here for the purpose of deleting the entire table, so all the commands can be seen in action===
# cursor.execute('''DROP TABLE book_inventory''')
# db.commit()

#===Create table===
cursor.execute('''
CREATE TABLE book_inventory (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
''')
db.commit()

cursor.execute('''
CREATE TABLE other_book_inventory (id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)
''')
db.commit()

cursor.execute('''
CREATE TABLE some_people_table (id INTEGER PRIMARY KEY, First_Name TEXT, Last_Name TEXT, Age INTEGER, email TEXT)
''')
db.commit()

data_for_people_table = []
for item in range(0, 20):
    id = item
    name = f"John{item}"
    l_name = f"Johnson{item}"
    age = 9 + item
    email = f"johnjohnson{item}@somemail.com"
    data_for_people_table.append((id, name, l_name, age, email))

cursor.executemany('''INSERT INTO some_people_table (id, First_Name, Last_Name, Age, email) VALUES(?, ?, ?, ?, ?)''', data_for_people_table)
db.commit()


books_to_commit = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30), 
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40), 
    (3003, 'The Lion, The Witch and the Wardrobe', 'C.S. Lewis', 25), 
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37), 
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]

#===Fill table with data===
cursor.executemany('''INSERT INTO book_inventory (id, Title, Author, Qty) VALUES(?, ?, ?, ?)''', books_to_commit)
db.commit()

#===some functions===
def new_entry():
    book_id = 3006
    book_title = "Widow"
    book_author = "Some Sad Widow"
    book_quantity = 1

    new_book_entry = (book_id, book_title, book_author, book_quantity)

    # write to database
    cursor.execute('''INSERT INTO book_inventory (id, Title, Author, Qty) VALUES(?, ?, ?, ?)''', new_book_entry)
    db.commit()


def update_info(balogney):
    # COMMAND to search for a specific book by one of it's parameters

    #-Update some info-
    book_title = "Widow"
    new_book_quantity = 2
    cursor.execute(balogney, (new_book_quantity, book_title))
    db.commit()

le_mayo = "UPDATE book_inventory SET Qty = ? WHERE Title = ?"

new_entry()

update_info(le_mayo)


#initial data in the table
cursor.execute('''SELECT * FROM book_inventory''')
books = cursor.fetchall()
print(f'\nInitial data in the table that is stored in a database')
print(books)

table_query = cursor.execute(f"SELECT name FROM sqlite_master WHERE type=\'table\';")
print(cursor.fetchall())