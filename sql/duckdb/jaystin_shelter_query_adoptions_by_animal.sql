SELECT animal_type, COUNT(*) AS adoption_count
FROM adoption

-- Organize by animal type to see which animals are adopted most frequently
GROUP BY animal_type
ORDER BY adoption_count DESC;
