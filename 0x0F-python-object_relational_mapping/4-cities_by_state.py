#!/usr/bin/python3
"""A module to print the cities by their states"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    U = argv[1]
    P = argv[2]
    D = argv[3]

    db = MySQLdb.connect(host='localhost', user=U, passwd=P, db=D)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
FROM cities INNER JOIN states ON cities.state_id = states.id \
ORDER BY cities.id")
    cities = cur.fetchall()

    for a in cities:
        print(a)
    cur.close()
    db.close()
