#!/usr/bin/python3
""" Scprit that lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    q_rows = cur.fetchall()
    for row in q_rows:
        print(row)
    cur.close()
    db.close()
