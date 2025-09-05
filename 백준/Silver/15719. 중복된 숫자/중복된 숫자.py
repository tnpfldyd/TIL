import sys

n = int(sys.stdin.readline())
s = 0
t = ""
for ch in sys.stdin.read():
    if ch.isdigit():
        t += ch
    elif ch == " ":
        s += int(t)
        t = ""
if t:
    s += int(t)
print(s - n * (n - 1) // 2)