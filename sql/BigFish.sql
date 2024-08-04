-- https://school.programmers.co.kr/learn/courses/30/lessons/298517

SELECT F.ID, F.LENGTH
FROM (
    SELECT ID, LENGTH, RANK() OVER (ORDER BY LENGTH DESC) as RNK
    FROM FISH_INFO
    ) F
WHERE F.RNK<11
ORDER BY F.RNK, F.ID
;