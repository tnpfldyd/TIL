import math
import sys
input = sys.stdin.readline

def calculate_operations(sequence, length):
    total_ops = 0
    ops_per_index = [0] * length
    for i in range(1, length):
        ratio = math.ceil(math.log2(sequence[i - 1] / sequence[i])) + ops_per_index[i - 1]
        if ratio > 0:
            ops_per_index[i] = max(0, ratio)
            total_ops += ops_per_index[i]
    return total_ops

sequence_length = int(input())
sequence = list(map(int, input().split()))
print(calculate_operations(sequence, sequence_length))