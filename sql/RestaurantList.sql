-- https://school.programmers.co.kr/learn/courses/30/lessons/131124

WITH reviewking AS (
    SELECT MEMBER_ID, COUNT(MEMBER_ID) as cnt
    FROM REST_REVIEW 
    GROUP BY MEMBER_ID
    ORDER BY 2 DESC
    LIMIT 1
)

SELECT m.MEMBER_NAME, rk.REVIEW_TEXT, date_format(rk.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM (SELECT r.* FROM REST_REVIEW r INNER JOIN reviewking k ON r.MEMBER_ID=k.MEMBER_ID) rk     
    LEFT JOIN MEMBER_PROFILE m ON rk.MEMBER_ID = m.MEMBER_ID
ORDER BY 3, 2
;
