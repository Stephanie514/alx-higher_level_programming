-- Script to convert the hbtn_0c_0 database, first_table, and the name field to UTF8MB4
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
