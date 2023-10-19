-- Create the 'unique_id' table in your MySQL server.
-- This table definition includes an 'id' column with a default value of 1
-- and a unique constraint, along with a 'name' column.

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
