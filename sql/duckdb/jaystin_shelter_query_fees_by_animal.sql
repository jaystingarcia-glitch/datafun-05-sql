-- Purpose: Calculate the average adoption fee for each animal type.

SELECT
    animal_type,
    AVG(fee) AS average_fee
FROM adoption
GROUP BY animal_type
ORDER BY average_fee DESC;
