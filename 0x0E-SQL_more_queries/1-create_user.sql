-- Create the MySQL server user user_0d_1 with all privileges
-- and set the password to user_0d_1_pwd if it doesn't already exist.

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
