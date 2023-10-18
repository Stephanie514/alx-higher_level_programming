-- Script to create the 'second_table' in the 'hbtn_0c_0' database and insert records
-- Usage: mysql -u your_username -p your_password -e "USE hbtn_0c_0; CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT); INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);"

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);
