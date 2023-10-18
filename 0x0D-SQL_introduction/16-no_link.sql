-- Script to list all records with names from 'second_table' in the specified database
-- This script does not specify the database name; it is provided as an argument when running the script
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
