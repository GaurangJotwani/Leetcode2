# Write your MySQL query statement below

SELECT p.project_id
FROM Project AS p
JOIN Employee AS E ON p.employee_id = e.employee_id
GROUP BY p.project_id
HAVING COUNT(*) = (SELECT COUNT(*)
FROM Project AS p
JOIN Employee AS E ON p.employee_id = e.employee_id
GROUP BY p.project_id
ORDER BY COUNT(*) DESC
LIMIT 1)


