-- Script to list records with a score >= 10 from 'second_table' in the 'hbtn_0c_0' database
-- Usage: mysql -u your_username -p your_password -e "USE hbtn_0c_0; SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;"
-- This script does not specify the database name; it is provided as an argument when running the script
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

