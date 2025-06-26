-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL (LEFT JOIN instruction)

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;