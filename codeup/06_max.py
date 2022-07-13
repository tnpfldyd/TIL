numbers = [0, 20, 100, 40]
# 0. 첫번째 숫자를 집어넣기
max_num = numbers[0]
# 1. 반복
for n in numbers:
    # 2. 만약, max 값이 n보다 작으면 바꾼다.
    if max_num < n:
        max_num = n
print(max_num)