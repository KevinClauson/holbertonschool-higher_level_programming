-- lists all genres in hbtn_0d_tvshows and displays the number of shows linked
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS shows
       FROM tv_genres INNER JOIN tv_show_genres
       ON tv_show_genres.genre_id = tv_genres.id
       GROUP BY tv_genres.name
       ORDER BY shows DESC;
