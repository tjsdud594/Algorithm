-- https://school.programmers.co.kr/learn/courses/30/lessons/299310

SELECT yearmax.YEAR
        , yearmax.MAX_SIZE - ori.SIZE_OF_COLONY AS YEAR_DEV
        , ori.ID
FROM ECOLI_DATA AS ori LEFT JOIN
    (SELECT MAX(SIZE_OF_COLONY) AS MAX_SIZE
            ,year(DIFFERENTIATION_DATE) AS YEAR
    FROM ECOLI_DATA 
    GROUP BY 2
    ) AS yearmax ON year(ori.DIFFERENTIATION_DATE) = yearmax.YEAR
ORDER BY yearmax.YEAR, YEAR_DEV
;