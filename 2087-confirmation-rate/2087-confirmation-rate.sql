# Write your MySQL query statement below

SELECT sn.user_id, ROUND(COALESCE(
    COUNT(
        CASE WHEN c.action = 'confirmed' THEN 1 END)
    / NULLIF(COUNT(c.user_id), 0)
,0), 2) AS 'confirmation_rate'
FROM Signups sn
LEFT JOIN Confirmations c on sn.user_id = c.user_id
GROUP BY sn.user_id