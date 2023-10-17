import sys
input = sys.stdin.readline

def check(a = True, b = True, c = True):
    global result
    if a and b and c:
        a -= 1
        b -= 1
        c -= 1
        result += 1
    return [a, b, c]
for _ in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().strip()))
    _ = input()
    result = 0
    numbers[0], numbers[1], _ = check(numbers[0], numbers[1])
    numbers[-1], numbers[-2], _ = check(numbers[-1], numbers[-2])
    for i in range(1, N - 1):
        numbers[i - 1], numbers[i], numbers[i + 1] = check(numbers[i - 1], numbers[i], numbers[i + 1])
    print(result)