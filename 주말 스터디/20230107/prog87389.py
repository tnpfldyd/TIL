def solution(n):
    n -= 1
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return i
    return n

print(solution(8))