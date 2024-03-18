#!/usr/bin/python3
"""A module to list all the states in a database"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    U = argv[1]
    P = argv[2]
    D = argv[3]

    data = MySQLdb.connect(host='localhost', user=U, passwd=P, db=D)
    cur = data.cursor()
    state = cur.execute("SELECT * FROM states WHERE name \
LIKE '{}' ORDER BY id".format(argv[4]))
    rows = cur.fetchall()
    for a in rows:
        print(a)
    cur.close()
    data.close()
