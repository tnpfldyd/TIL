T = 10
W, K = [], []
for i in range(T):
    W_score = int(input())
    W.append(W_score)
for i in range(T):
    K_score = int(input())
    K.append(K_score)
W = sorted(W, reverse = True)
K = sorted(K, reverse = True)
print(sum(W[0:3]), sum(K[0:3]))
