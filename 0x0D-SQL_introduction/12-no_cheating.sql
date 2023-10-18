-- Script to update Bob's score to 10 in 'second_table' of the specified database
-- Usage: mysql -u your_username -p your_password -e "USE your_database; UPDATE second_table SET score = 10 WHERE name = 'Bob';"
-- This script does not specify the database name; it is provided as an argument when running the script
UPDATE second_table SET score = 10 WHERE name = 'Bob';
