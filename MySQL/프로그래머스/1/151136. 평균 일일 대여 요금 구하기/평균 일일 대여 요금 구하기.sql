-- CAR_ID: 자동차 ID 
-- CAR_TYPE: 자동차 종류 ('세단', 'SUV', '승합차', '트럭', '리무진')
-- DAILY_FEE: 일일 대여 요금(원)
-- OPTIONS: 자동차 옵션 리스트 ('주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트')

SELECT ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';