-- Script to display the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- This script does not specify the database name; it is provided as an argument when running the script
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
