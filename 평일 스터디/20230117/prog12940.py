def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    result = (a * b) // gcd(a, b)
    return result
def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))
    return answer

print(solution(3, 12))