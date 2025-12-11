V = input().strip()

uc = V.count('U') + V.count('C')
dp = V.count('D') + V.count('P')

result = []

if uc > (dp + 1) // 2:
    result.append('U')

if dp > 0:
    result.append('D')
    result.append('P')

print(''.join(result) if result else 'C')