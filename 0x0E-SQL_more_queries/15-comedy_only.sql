-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT title
FROM tv_genres
LEFT JOIN tv_show_genres ON genre_id = tv_genres.id
LEFT JOIN tv_shows ON show_id = tv_shows.id
WHERE name = "Comedy"
ORDER BY title ASC;
