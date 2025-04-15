import sys

def is_surprising(s):
    n = len(s)
    for d in range(n - 1):
        seen = set()
        for i in range(n - d - 1):
            pair = s[i] + s[i + d + 1]
            if pair in seen:
                return False
            seen.add(pair)
    return True

while True:
    line = sys.stdin.readline().strip()
    if line == "*":
        break
    result = "surprising" if is_surprising(line) else "NOT surprising"
    print(f"{line} is {result}.")