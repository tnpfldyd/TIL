import sys

input = sys.stdin.readline

MAX = 100001

def main():
	N, K = map(int, input().split())
	bulbs = [0] + list(map(int, input().split()))
	
	xor_bulbs = [0] * (MAX + 1)
	for i in range(1, N + 1):
		xor_bulbs[i] = bulbs[i - 1] ^ bulbs[i]
	
	toggle_count = 0
	for i in range(1, N - K + 2):
		if xor_bulbs[i]:
			xor_bulbs[i] ^= 1
			xor_bulbs[i + K] ^= 1
			toggle_count += 1
	
	for i in range(N - K + 2, N + 1):
		if xor_bulbs[i]:
			print("Insomnia")
			return
	
	print(toggle_count)

if __name__ == "__main__":
	main()