-- a script to select by the foreign key
SELECT id, name 
FROM cities
WHERE state_id = SELECT id FROM states
WHERE name LIKE 'California';
