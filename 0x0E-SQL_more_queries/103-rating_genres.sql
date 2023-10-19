-- Retrieve and list all TV show genres from the hbtn_0d_tvshows_rate database, ordered by their average rating.

USE hbtn_0d_tvshows_rate;

SELECT tv_genres.name, AVG(tv_show_ratings.rate) AS 'average_rating'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY average_rating DESC;
