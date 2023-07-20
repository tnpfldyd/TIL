S, T = list(input()), list(input())

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1]
        T = T[::-1]

for i in range(len(S)):
    if S[i] != T[i]:
        print(0)
        break
else:
    print(1)