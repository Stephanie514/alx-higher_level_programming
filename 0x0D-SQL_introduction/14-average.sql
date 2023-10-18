-- Script to compute the average score of all records in 'second_table' of the specified database
-- Usage: mysql -u your_username -p your_password -e "USE your_database; SELECT AVG(score) AS average FROM second_table;"
-- This script does not specify the database name; it is provided as an argument when running the script
SELECT AVG(score) AS average FROM second_table;
