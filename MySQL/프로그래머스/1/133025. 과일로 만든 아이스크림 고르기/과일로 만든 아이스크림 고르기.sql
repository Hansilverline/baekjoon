-- FIRST_HALF 테이블 
-- SHIPMENT_ID: 아이스크림 공장에서 아이스크림 가게까지의 출하 번호
-- FLAVOR: 아이스크림 맛
-- TOTAL_ORDER: 상반기 아이스크림 총주문량

-- ICECREAM_INFO 테이블
-- FLAVOR: 아이스크림 맛
-- INGREDITENT_TYPE: 아이스크림의 성분 타입 (sugar_based, fruit_based)

SELECT F.FLAVOR 
FROM FIRST_HALF AS F 
JOIN ICECREAM_INFO AS I ON F.FLAVOR = I.FLAVOR
WHERE (F.TOTAL_ORDER > 3000) AND (I.INGREDIENT_TYPE = 'fruit_based')
ORDER BY TOTAL_ORDER DESC;

-- WHERE (A.TOTAL_ORDER > 3000) AND (B.INGREDIENT_TYPE = 'fruit_based')
-- ORDER BY A.TOTAL_ORDER DESC