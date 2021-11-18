-- that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv.shows.title, tv.shows_genres.genre_id FROM tv.shows
LEFT JOIN tv.shows_genres ON tv.shows.id = tv.shows_genres.show_id
ORDER BY title, genre_id;
