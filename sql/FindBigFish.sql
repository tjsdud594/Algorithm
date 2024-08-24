-- https://school.programmers.co.kr/learn/courses/30/lessons/293261

WITH max_f as (SELECT FISH_TYPE, max(LENGTH) as LENGTH
FROM FISH_INFO 
GROUP BY FISH_TYPE
),

name_f as (
    SELECT info.ID, max_f.FISH_TYPE, max_f.LENGTH
    FROM FISH_INFO info LEFT JOIN max_f ON info.FISH_TYPE=max_f.FISH_TYPE
    WHERE info.FISH_TYPE=max_f.FISH_TYPE AND info.LENGTH=max_f.LENGTH
)

SELECT n.ID, nn.FISH_NAME, n.LENGTH
FROM name_f n LEFT JOIN FISH_NAME_INFO nn ON n.FISH_TYPE=nn.FISH_TYPE
ORDER BY 1
;