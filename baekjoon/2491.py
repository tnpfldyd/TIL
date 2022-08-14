T = int(input())
num = list(map(int, input().split()))
result1 = [1] * T # 오름
result2 = [1] * T # 내림
for i in range(1, T):
    if num[i] >= num[i - 1]:
        result1[i] = max(result1[i], result1[i - 1] + 1)
    if num[i] <= num[i - 1]:
        result2[i] = max(result2[i], result2[i - 1] + 1)
print(max(max(result1), max(result2)))