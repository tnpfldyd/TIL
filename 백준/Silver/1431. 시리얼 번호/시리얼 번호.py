import sys
input = sys.stdin.readline

def get_digit_sum(s):
    return sum(int(c) for c in s if c.isdigit())

def compare_key(s):
    return (len(s), get_digit_sum(s), s)

N = int(input())
serials = []
for _ in range(N):
    serials.append(input().strip())

serials.sort(key=compare_key)

for serial in serials:
    print(serial)