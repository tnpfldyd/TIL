A = input().strip()
B = input().strip()

print(''.join('1' if a == '1' and b == '1' else '0' for a, b in zip(A, B)))
print(''.join('1' if a == '1' or b == '1' else '0' for a, b in zip(A, B)))
print(''.join('1' if a != b else '0' for a, b in zip(A, B)))
print(''.join('0' if a == '1' else '1' for a in A))
print(''.join('0' if b == '1' else '1' for b in B))