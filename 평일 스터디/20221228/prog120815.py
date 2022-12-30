def gcd(a, b):
    if not b:
        return a
    if not a % b:
        return b
    return gcd(b, a % b)

def solution(n):
    answer = (n*6//gcd(n,6))//6
    return answer

print(solution(10))