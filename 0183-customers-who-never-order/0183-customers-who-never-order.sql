# Write your MySQL query statement below
SELECT name as Customers FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE c.id = o.customerId)