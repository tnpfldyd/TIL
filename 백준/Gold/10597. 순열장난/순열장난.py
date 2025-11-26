import sys
input = sys.stdin.readline
s = input().strip()
length = len(s)

def solve(index, current_list):
    if index == length:
        if max(current_list) == len(current_list):
            print(*current_list)
            sys.exit()
        return

    if index < length:
        num = int(s[index])
        if num > 0 and num not in current_list:
            solve(index + 1, current_list + [num])

    if index + 1 < length:
        num = int(s[index:index+2])
        if num <= 50 and num not in current_list and s[index] != '0':
            solve(index + 2, current_list + [num])

solve(0, [])