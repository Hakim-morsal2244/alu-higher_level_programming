-- Lists all genres and the number of shows linked to each
-- Results are sorted in descending order by the number of shows linked
SELECT tv_show_genres.genre_id, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY tv_show_genres.genre_id
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
