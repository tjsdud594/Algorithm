-- https://school.programmers.co.kr/learn/courses/30/lessons/284531

SELECT ROUTE
        , concat(round(sum(D_BETWEEN_DIST), 1), "km") AS TOTAL_DISTANCE
        , concat(round(avg(D_BETWEEN_DIST), 2), "km") AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE ori
GROUP BY ROUTE
ORDER BY sum(D_BETWEEN_DIST) desc
;