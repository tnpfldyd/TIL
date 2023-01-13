
def knumber(x, num):
    number = ''
    while x:
        number += str(x%num)
        x //= num
    return number[::-1]

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if not x % i:
            return False
    return True

def solution(n, k):
    answer = knumber(n, k).split('0')
    result = 0
    for num in answer:
        if num and is_prime(int(num)):
            result += 1
    return result