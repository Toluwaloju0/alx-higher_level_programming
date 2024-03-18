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

    cur.execute(f"SELECT cities.name FROM cities WHERE cities.state_id = (\
SELECT id FROM states WHERE name LIKE '{argv[4]}')")
    cities = cur.fetchall()

    for a in range(len(cities)):
        if a == len(cities) - 1:
            print(cities[a][0])
            break
        print(cities[a][0] + ', ', end="")
    cur.close()
    db.close()
