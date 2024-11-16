-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT tv_shows.title, SUM(tv_ratings.rating) AS rating
FROM tv_shows
JOIN tv_ratings ON tv_shows.id = tv_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
