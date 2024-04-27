--A script to add a new column for the average scores
ALTER TABLE second_table
  ADD COLUMN (average INT);
INSERT INTO second_table VALUES
  (SELECT AVG score FROM second_table);
