-- https://school.programmers.co.kr/learn/courses/30/lessons/301650

SELECT th.First as ID
FROM (
    SELECT s.ID AS First 
        , s.PARENT_ID AS Second 
        , t.PARENT_ID AS Third
    FROM ECOLI_DATA s INNER JOIN ECOLI_DATA t
        ON s.PARENT_ID=t.ID
    WHERE t.PARENT_ID IS NOT NULL
) th INNER JOIN ECOLI_DATA f 
    ON th.Third=f.ID
WHERE f.PARENT_ID IS NULL
ORDER BY th.First
;