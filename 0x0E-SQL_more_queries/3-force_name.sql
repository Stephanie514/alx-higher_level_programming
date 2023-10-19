-- Create the force_name table in the specified database
-- Table description: id INT, name VARCHAR(256) (not null)
-- The database name will be passed as an argument to the mysql command
-- Replace 'your_database_name' with the actual database name

USE your_database_name

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
-- Insert initial data if the table doesn't exist
-- You can modify the values as needed

INSERT IGNORE INTO force_name (id, name)
VALUES (1, 'ExampleName1'),
       (2, 'ExampleName2');
