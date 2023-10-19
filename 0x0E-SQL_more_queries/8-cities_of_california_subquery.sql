-- List all the cities of California from the hbtn_0d_usa database
-- without using JOIN and sort the results in ascending order by cities.id.

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
