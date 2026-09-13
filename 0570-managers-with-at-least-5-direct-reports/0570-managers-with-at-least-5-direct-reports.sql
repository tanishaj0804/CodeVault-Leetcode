# Write your MySQL query statement below
SELECT m.name FROM employee e JOIN employee m ON e.managerId = m.id GROUP BY e.managerId HAVING COUNT(e.id) >= 5