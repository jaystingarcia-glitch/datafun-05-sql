-- Purpose: Count how many adoptions occurred on each date.

SELECT
    adopt_date,
    COUNT(*) AS adoption_count
FROM adoption
GROUP BY adopt_date
ORDER BY adopt_date;
