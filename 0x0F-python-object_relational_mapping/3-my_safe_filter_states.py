#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    import MySQLdb

    argv = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
