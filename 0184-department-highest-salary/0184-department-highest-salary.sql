# Write your MySQL query statement below
WITH maxsaldept as (SELECT d.name as Department, e.name as employee, e.salary, DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rnk FROM Employee as e JOIN Department as d ON e.departmentId = d.id)
SELECT department, employee, salary FROM maxsaldept WHERE rnk = 1