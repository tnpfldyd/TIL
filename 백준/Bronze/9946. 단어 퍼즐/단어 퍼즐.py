import sys
from collections import Counter

input = sys.stdin.readline
case = 0

while (a := input().strip()) + (b := input().strip()) != "ENDEND":
    case += 1
    print(f"Case {case}: {'same' if Counter(a) == Counter(b) else 'different'}")