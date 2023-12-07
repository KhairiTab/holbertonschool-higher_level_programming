--script that lists all records of the table 
-- where name is not null 
--order by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY number DESC;