import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    numbers = list(map(int, input().split()))
    numbers.sort()
    if numbers[3] - numbers[1] >= 4:
        print("KIN")
        continue
    print(sum(numbers[1:4]))