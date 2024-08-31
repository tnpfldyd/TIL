import sys
input = sys.stdin.readline

def max_score(arr, n):
    if n == 1:
        return arr[0]
    
    score = 0
    for i in range(0, n-1, 2):
        a, b = arr[i], arr[i+1]
        if a < 0 and b < 0:
            score += a * b
        else:
            if a < 0 and b > 0:
                score += a
            break
    
    if i+2 == n-1:
        if arr[n-1] < 0:
            score += arr[n-1]
    
    add_idx = 0
    for i in range(n-1, 0, -2):
        a, b = arr[i], arr[i-1]
        if a > 1 and b > 1:
            score += a * b
        else:
            add_idx = i
            break
    
    for i in range(add_idx, -1, -1):
        if arr[i] >= 1:
            score += arr[i]
        else:
            break
    
    return score

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort()
    print(max_score(arr, n))