-- Subquery
SELECT id, name FROM cities
WHERE state_id IN (select id FROM states WHRERE name = "California")
ORDER BY 1;
