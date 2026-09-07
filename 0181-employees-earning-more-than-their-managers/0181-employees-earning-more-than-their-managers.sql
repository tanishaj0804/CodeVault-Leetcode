# Write your MySQL query statement below
SELECT e.name as employee From Employee e JOIN Employee m  on e.managerId = m.id 
WHERE e.salary > m.salary