-- Script to remove records with score <= 5 from 'second_table' in the specified database
-- Usage: mysql -u your_username -p your_password -e "USE your_database; DELETE FROM second_table WHERE score <= 5;"
-- This script does not specify the database name; it is provided as an argument when running the script
DELETE FROM second_table WHERE score <= 5;
