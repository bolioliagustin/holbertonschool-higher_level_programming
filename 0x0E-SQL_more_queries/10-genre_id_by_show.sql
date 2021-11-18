--  that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv.shows.title, tv.show_genres.genre_id FROM tv.shows
JOIN tv.show_genres ON tv.shows.id = tv.show_genres.show_id
GROUP BY tv.shows.title, tv.show_genres.genre_id
ORDER BY tv.shows.title ASC;