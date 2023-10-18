-- Script to display the number of records with id = 89 in 'first_table' of the 'hbtn_0c_0' database
-- Usage: mysql -u your_username -p your_password -e "USE hbtn_0c_0; SELECT COUNT(*) FROM first_table WHERE id = 89;"
-- This script does not specify the database name; it is provided as an argument when running the script
SELECT COUNT(*) FROM first_table WHERE id = 89;
