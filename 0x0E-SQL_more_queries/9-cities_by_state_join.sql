-- List all cities in the hbtn_0d_usa database along with their states.
 -- Replace with the actual database name
USE hbtn_0d_usa;

SELECT CONCAT(cities.id, ' - ', cities.name, ' - ', states.name) AS CityInfo
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
