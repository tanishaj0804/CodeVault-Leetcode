# Write your MySQL query statement below
SELECT id FROM (SELECT id,temperature,recordDate,LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp, LAG(recordDate) OVER (ORDER BY recordDate) as prev_Date FROM Weather) AS t
WHERE temperature > prev_temp AND DATEDIFF(recordDate, prev_date) = 1 
#else join weather table twice and do the comparisons where date difference b/w then is 1, and weather2 table's temp is higher than weather1 table's temp