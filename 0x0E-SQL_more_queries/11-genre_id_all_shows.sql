-- Retrieve all shows from the hbtn_0d_tvshows database along with their genres (if any).

USE hbtn_0d_tvshows; -- Replace with the actual database name

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
