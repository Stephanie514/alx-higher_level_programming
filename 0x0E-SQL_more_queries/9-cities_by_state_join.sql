-- List all cities in the hbtn_0d_usa database along with their states.

USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
