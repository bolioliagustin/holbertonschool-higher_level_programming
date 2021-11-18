--  that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tv.shows.title, tv.shows_genre.genre_id FROM tv_shows
LEFT JOIN tv.shows_genre ON tv.shows.id = tv.shows_genre.show_id
WHERE genre_id IS NULL;
ORDER BY title, genre_id ASC;