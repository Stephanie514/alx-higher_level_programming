-- Script to convert the hbtn_0c_0 database and set character set and collation for first_table
-- This script does not specify the database name; it is provided as an argument when running the script
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
