-- A script to list scores and names
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
