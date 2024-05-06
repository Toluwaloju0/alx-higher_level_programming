-- a script to select by the foreign key
SELECT cities.id, cities.name FROM cities WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = "California");
