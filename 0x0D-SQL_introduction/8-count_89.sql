-- Count items
SELECT COUNT(*)
FROM first_table
GROUP BY id
HAVING id = 89;
