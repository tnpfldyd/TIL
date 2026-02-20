import sys
input = sys.stdin.readline
n = int(input())
string = input().strip()
print('J' * string.count('J') + 'O' * string.count('O') + 'I' * string.count('I'))