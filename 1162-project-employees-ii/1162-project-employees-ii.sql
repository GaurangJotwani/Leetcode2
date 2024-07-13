WITH ProjectEmployeeCount AS (
    SELECT p.project_id, COUNT(*) AS employee_count
    FROM Project AS p
    JOIN Employee AS E ON p.employee_id = e.employee_id
    GROUP BY p.project_id 
)
SELECT project_id
FROM ProjectEmployeeCount
WHERE employee_count = (SELECT MAX(employee_count) FROM ProjectEmployeeCount)

-- WITH ProjectEmployeeCount AS (
--     SELECT p.project_id, COUNT(*) AS employee_count
--     FROM Project AS p
--     JOIN Employee AS E ON p.employee_id = e.employee_id
--     GROUP BY p.project_id
-- )
-- SELECT project_id
-- FROM ProjectEmployeeCount
-- WHERE employee_count = (
--     SELECT MAX(employee_count)
--     FROM ProjectEmployeeCount
-- );

