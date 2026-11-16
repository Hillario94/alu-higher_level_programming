-- Display the top 3 cities temperature during July and August
SELECT city, AVG(temperature) AS avg_temp FROM temps WHERE MONTH(date) IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
