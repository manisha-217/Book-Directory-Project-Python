import sqlite3
def connect():
    ##creat database and add table
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("CREATE TABLE IF NOT EXISTS"
            "book (id integer PRIMARY KEY"
                   "title text,"
                   "author text,"
                   "year integer"
                   "isbn integer)")
    db.commit()
    db.close()
def insert(title,author,year,isbn):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.execute("INSERT INTO book"
              "value (NULL,?,?,?,?)",(title,author,year,isbn))
    db.commit()
    db.close()
              
def view():
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.excute("Select * FROM book")
    rows = t.fetchall()
    db.close()
def search(title="",author="",year="",isbn=""):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.excute("SELECT * "
             "FROM book"
             "WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    row=t.fetchall()     
    db.close()
def update(title,author,year,isbn):
    db=sqlite3.connect("water.db")
    t=db.cursor()
    t.excute(

        )
    db.commit()
    db.close()
def delete():
    db=sqlite3.connect(water.db)
    t=db.cursor()
    t.excute(

        )
    db.commit()
    db.close()

connect()
