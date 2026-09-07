# Write your MySQL query statement below
SELECT DISTINCT num as ConsecutiveNums FROM (SELECT num, LAG(num) over ( ORDER BY id) as prev, LEAD(num) over (order by id) as next FROM logs) t 
WHERE prev = num and next = num