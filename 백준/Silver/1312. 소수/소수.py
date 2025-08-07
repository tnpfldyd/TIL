A, B, N = map(int, input().split())
remainder = A % B
for i in range(N):
    remainder *= 10
    digit = remainder // B
    remainder = remainder % B
print(digit)