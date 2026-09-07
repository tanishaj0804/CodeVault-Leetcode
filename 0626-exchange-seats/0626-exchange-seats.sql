# Write your MySQL query statement below
SELECT id, CASE 
            WHEN id%2 = 0 THEN LAG(student) OVER (order by id)
            ELSE COALESCE(LEAD(student) OVER (ORDER BY id), student)
            END
            as student 
            FROM seat