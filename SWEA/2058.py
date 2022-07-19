T = int(input())
result = 0
while T:
    result += T % 10
    T //= 10
print(result)