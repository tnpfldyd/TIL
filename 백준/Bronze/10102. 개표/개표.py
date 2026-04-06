input()
s = input().strip()

a = s.count('A')
b = s.count('B')

print('A' if a > b else 'B' if b > a else 'Tie')