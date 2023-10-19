-- Create the 'unique_id' table in the MySQL server.
-- This table will have an 'id' column with a default value of 1, and a unique constraint,
-- and a 'name' column.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
