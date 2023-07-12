n = int(input())
v = list(map(int, input().split()))

v.sort()

answer = float('inf')
for i in range(n - 3):
    for j in range(i + 3, n):
        left = i + 1
        right = j - 1
        
        while left < right:
            a = v[i] + v[j]
            b = v[left] + v[right]
            diff = b - a
            
            answer = min(answer, abs(diff))

            if diff > 0:
                right -= 1
            else:
                left += 1

print(answer)