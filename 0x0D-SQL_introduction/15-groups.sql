-- A script to count the number of scores in a table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
