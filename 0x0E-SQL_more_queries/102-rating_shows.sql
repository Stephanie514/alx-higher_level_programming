-- Retrieve and list all TV shows from the hbtn_0d_tvshows_rate database, sorted by their overall ratings.
SELECT title, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY title
ORDER BY rating DESC;
