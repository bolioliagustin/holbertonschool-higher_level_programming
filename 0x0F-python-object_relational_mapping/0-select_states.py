import MySQLdb
import sys

argv = sys.argv
db = MySQLdb.connect(host="localhost", port = 3306, user = argv[1], passwd = argv[2], db = argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
db.close()
