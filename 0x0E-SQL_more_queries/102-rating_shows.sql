-- Retrieve and list all TV shows from the hbtn_0d_tvshows_rate database, sorted by their overall ratings.

USE hbtn_0d_tvshows_rate;

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
