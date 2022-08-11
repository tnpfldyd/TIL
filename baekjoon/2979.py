A, B, C = map(int, input().split())
result = [0] * 101
for i in range(3):
    IN, OUT = map(int, input().split())
    for j in range(IN, OUT):
        result[j] += 1
cnt = 0
for i in range(101):
    if result[i] == 1:
        cnt += A
    elif result[i] == 2:
        cnt += B * 2
    elif result[i] == 3:
        cnt += C * 3
print(cnt)