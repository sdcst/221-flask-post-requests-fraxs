#!python3

import sqlite3
db = None

def createTable(cursor):
    query = """create table if not exists Test (
        id integer primary key,
        data tinytext
    )
    """
    cursor.execute(query)
    return FileNotFoundError

def addData(cursor,db):
    data = ['Happy Birthday','Twinkle Twinkle Little Star','Humpty Dumpty','Have a Merry Christmas','The Boulevard of Broken Dreams','Walking with a Ghost']
    for i in data:
        query = f'insert into Test (data) values ("{i}")'
        cursor.execute(query)
    

def get(cursor):
    queries = [
        "T%",
        "The%",
        "%of%",
        "%erry",
        "%erry%",
        "H%mpt%ty",
        "H%mpty",
        "%"

    ]
    for i in queries:
        q = f"select * from Test where data like '{i}'"
        r = cursor.execute(q)
        data = list(r)
        print(i, data)

def main():
    db = sqlite3.connect("test.db")
    cursor = db.cursor()
    createTable(cursor)
    #addData(db,cursor)
    #db.commit()
    get(cursor)

if __name__ == "__main__":
    main()