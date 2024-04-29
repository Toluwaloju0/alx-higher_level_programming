-- a script to select by the foreign key
SELECT id, name WHERE state_id = SELECT states.id WHERE states.name LIKE 'California';
