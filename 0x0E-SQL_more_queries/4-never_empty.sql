-- Create the 'id_not_null' table in the MySQL server.
-- This table will have an 'id' column with a default value of 1, and a 'name' column.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
