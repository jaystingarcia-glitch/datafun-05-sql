-- Purpose: Show each outcome type and how many records fall under each one.

SELECT outcome, COUNT(*) AS outcome_count
FROM adoption
GROUP BY outcome
ORDER BY outcome_count DESC;
