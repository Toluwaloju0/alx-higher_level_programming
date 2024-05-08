-- A script to count genres from a show and list them
SELECT tv_genres.name as genre, COUNT(tv_show_genres.genre_id) as number_of_shows FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(tv_show_genres.genre_id) DESC;
