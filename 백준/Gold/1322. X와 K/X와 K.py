X, K = map(int, input().split())
Y = 0
bit = 1
while K:
    while X & bit:
        bit <<= 1
    if K & 1:
        Y |= bit
    K >>= 1
    bit <<= 1
print(Y)