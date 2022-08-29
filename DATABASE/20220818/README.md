# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
CREATE TABLE healthcare (
id PRIMARY KEY,        
sido INTEGER NOT NULL, 
gender INTEGER NOT NULL,
age INTEGER NOT NULL,  
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,   
va_left REAL NOT NULL, 
va_right REAL NOT NULL,

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE age < 10;
```

```
COUNT(*)
--------
156277
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE gender = 1;
```

```
COUNT(*)
--------
510689
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE smoking = 3 and is_drinking = 1;
```

```
COUNT(*)
--------
150361
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare WHERE va_left >= 2.0 and va_right >= 2.0;
```

```
COUNT(*)
--------
2614
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```

```
sido
----
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 36 도시에 살면서 키는 180 초과 몸무게는 80 초과 허리둘레는 90 초과 담배 피는 사람
```sql
SELECT COUNT(*) FROM healthcare WHERE sido = 36 and height > 180 and weight > 80 and waist > 90 and smoking > 0;
```
```
COUNT(*)
--------
19
```
키가 100 이하이거나 몸무게가 50 이하인 사람
```sql
SELECT COUNT(*) FROM healthcare WHERE height <= 100 or weight <= 50;
```
```
COUNT(*)
--------
204250
```
나이의 총 가지수는?
```sql
SELECT COUNT(DISTINCT age) FROM healthcare;
```

```
COUNT(DISTINCT age)
-------------------
10
```
나이가 18살 이면서 키가 180이상 인사람은?
```slq
SELECT COUNT(*) FROM healthcare WHERE age = 18 and height >= 180;
```

```
COUNT(*)
--------
4
```
BMI로 칼럼을 지정해서 계산 값을 보여주고 weight와 height를 보여줘 1~5번까지
```slq
SELECT weight*10000/(height*height) AS BMI, weight, height FROM healthcare LIMIT 5;