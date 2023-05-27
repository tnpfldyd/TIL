-- 코드를 입력하세요
SELECT a.animal_id, b.name FROM animal_ins AS a
JOIN animal_outs AS b
ON a.animal_id = b.animal_id
WHERE a.datetime > b.datetime
ORDER BY a.datetime