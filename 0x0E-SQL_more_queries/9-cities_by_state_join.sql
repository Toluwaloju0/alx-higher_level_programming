-- a script to join two tables
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
