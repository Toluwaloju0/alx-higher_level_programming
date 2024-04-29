-- A script to create a table with a unique id value if null
CREATE TABLE IF NOT EXISTS unique_id(
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
    );
