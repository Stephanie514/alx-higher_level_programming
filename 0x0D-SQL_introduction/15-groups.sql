-- Script to list the number of records with the same score in 'second_table' of the specified database
-- Usage: mysql -u your_username -p your_password -e "USE your_database; SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;"
-- This script does not specify the database name; it is provided as an argument when running the script
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
