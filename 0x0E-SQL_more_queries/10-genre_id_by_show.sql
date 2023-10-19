-- List all shows in hbtn_0d_tvshows with at least one linked genre.
 -- Replace with the actual database name
USE hbtn_0d_tvshows;

SELECT DISTINCT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
