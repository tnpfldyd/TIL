import sys
input = sys.stdin.readline

while (N := int(input())):
    print(min((input().strip() for _ in range(N)), key=str.lower))