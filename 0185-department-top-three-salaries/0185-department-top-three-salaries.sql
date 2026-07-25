# Write your MySQL query statement below
SELECT Department, Employee, Salary from
(SELECT d.name as Department, e.name as Employee, Salary, DENSE_RANK() OVER (PARTITION BY DepartmentId ORDER BY Salary Desc) as rnk FROM Employee e JOIN Department d ON e.departmentId = d.id ) t
Where rnk <= 3