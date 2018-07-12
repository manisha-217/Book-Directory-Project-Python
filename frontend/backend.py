import sqlite3
def connect():
    ##creat database and add table
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("CREATE TABLE IF NOT EXISTS "
            "book (id integer PRIMARY KEY AUTOINCREMENT,"
                   "title text,"
                   "author text,"
                   "year integer,"
                   "isbn integer)")
    db.commit()
    db.close()
def insert(title,author,year,isbn):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("INSERT INTO book (title , author , year , isbn) "
                    "VALUES (?, ?, ?, ?)", (title, author, year, isbn,))

    db.commit()
    db.close()
              
def view():
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("Select * FROM book")
    rows = t.fetchall()
    db.close()
    return rows
def search(title = "",author = "",year = "",isbn = ""):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    row=t.fetchall()     
    db.close()
    return row
def update1(id,title,author,year,isbn):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("UPDATE book set title = ?, author = ?, year = ?, isbn = ? WHERE id = ?",(title,author,year,isbn,id))
    db.commit()
    db.close()
def delete(id):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("DELETE FROM book "
             "WHERE id= ?",(id,))
    db.commit()
    db.close()

connect()
