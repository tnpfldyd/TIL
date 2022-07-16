n=int(input())
result = 0

for i in range(n+1):
    result += i
    if result >= n:
        print(i)
        break
