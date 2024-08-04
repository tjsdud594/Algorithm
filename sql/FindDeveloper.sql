-- https://school.programmers.co.kr/learn/courses/30/lessons/276034
-- 비트연산자

SELECT dev.ID, dev.EMAIL, dev.FIRST_NAME, dev.LAST_NAME
FROM (
    SELECT *
        , (SELECT CODE FROM SKILLCODES WHERE NAME='Python') AS python
        , (SELECT CODE FROM SKILLCODES WHERE NAME='C#') AS c
    FROM DEVELOPERS 
    ) dev
WHERE (dev.SKILL_CODE&dev.python)=dev.python or (dev.SKILL_CODE&dev.c)=dev.c
ORDER BY dev.ID
;