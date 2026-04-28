n = input().strip()
mid = len(n) // 2

left = sum(map(int, n[:mid]))
right = sum(map(int, n[mid:]))

print("LUCKY" if left == right else "READY")