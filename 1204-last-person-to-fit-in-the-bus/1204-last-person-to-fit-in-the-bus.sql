# Write your MySQL query statement below
WITH x AS (SELECT turn,person_name,SUM(weight) OVER (ORDER BY turn) as running_total FROM queue)
SELECT person_name FROM x where running_total <= 1000 order by turn desc LIMIT 1