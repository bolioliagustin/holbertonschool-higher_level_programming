#!/usr/bin/python3
""" script that lists all states with from the database
hbtn_0e_6_usa where name matches the argument. """


if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = sys.argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                ORDER BY states.id ASC".format(argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
