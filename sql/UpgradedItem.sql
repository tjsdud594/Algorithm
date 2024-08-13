-- https://school.programmers.co.kr/learn/courses/30/lessons/273711


SELECT f.ITEM_ID, f.ITEM_NAME, f.RARITY
FROM (
    SELECT t.ITEM_ID, r.ITEM_NAME
    FROM ITEM_TREE t 
        LEFT JOIN (
        SELECT ITEM_ID, ITEM_NAME, RARITY
        FROM ITEM_INFO
        WHERE RARITY='RARE'
        ) r ON t.PARENT_ITEM_ID = r.ITEM_ID
    WHERE r.ITEM_NAME IS NOT NULL
) upg LEFT JOIN ITEM_INFO f ON upg.ITEM_ID = f.ITEM_ID
ORDER BY f.ITEM_ID DESC
;