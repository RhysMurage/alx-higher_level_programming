-- at displays the average temperature
-- ordered by temperature descending
SELECT AVG(value) AS avg_temp
	FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
	
