SELECT C.NAME NAME, C.PRICE * COUNT(*) CNT 
FROM CHARACTERS C 
LEFT OUTER JOIN PURCHASES P
ON C.NAME = P.ITEM 
GROUP BY C.NAME 
ORDER BY C.NAME;