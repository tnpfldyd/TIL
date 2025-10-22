import sys
input = sys.stdin.readline

S = input().strip()

i = 0
possible = True

while i < len(S):
    if i + 2 <= len(S) and S[i:i+2] == "pi":
        i += 2
    elif i + 2 <= len(S) and S[i:i+2] == "ka":
        i += 2
    elif i + 3 <= len(S) and S[i:i+3] == "chu":
        i += 3
    else:
        possible = False
        break
        
print("YES" if possible else "NO")