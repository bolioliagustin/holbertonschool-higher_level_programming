--  that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY name
ORDER BY number_of_shows DESC;