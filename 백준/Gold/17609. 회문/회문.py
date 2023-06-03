import sys
input = sys.stdin.readline

T = int(input())

def check_palindrome(l, r, flag):
    while l < r:
        if check_string[l] == check_string[r]:
            l += 1
            r -= 1
        else:
            if not flag:
                if not check_palindrome(l + 1, r, True) or not check_palindrome(l, r - 1, True):
                    return 1
            return 2
    return 0

for _ in range(T):
    check_string = input().strip()
    print(check_palindrome(0, len(check_string) - 1, False))