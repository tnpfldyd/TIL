class Heap:
    def __init__(self, n, k, p):
        self.heap = [0] * (n + 1)
        self.n = n
        self.k = k
        self.p = p
        self.upnum = 0
        self.downnum = k - 1
        self.heapnum = 0

    def dfs(self, idx):
        self.downnum += 1
        if self.downnum > self.n:
            print(-1)
            exit(0)
        self.heap[idx] = self.downnum
        if idx * 2 <= self.n:
            self.dfs(idx * 2)
        if idx * 2 + 1 <= self.n:
            self.dfs(idx * 2 + 1)

    def upheap(self, idx):
        while idx > 1:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx //= 2

    def insert(self, idx):
        self.heapnum += 1
        if self.heapnum == self.upnum:
            self.heapnum = self.downnum + 1
        self.heap[idx] = self.heapnum
        self.upheap(idx)
        if idx * 2 <= self.n:
            self.insert(idx * 2)
        if idx * 2 + 1 <= self.n:
            self.insert(idx * 2 + 1)

def main():
    N = int(input())
    K, P = map(int, input().split())
    heap = Heap(N, K, P)
    heap.dfs(P)
    heap.upnum = K
    while P // 2 > 0:
        P //= 2
        heap.upnum -= 1
        heap.heap[P] = heap.upnum
    if heap.upnum <= 0:
        print(-1)
        return

    for i in range(1, N + 1):
        if heap.heap[i] == 0:
            heap.insert(i)

    for i in range(1, N + 1):
        print(heap.heap[i])

if __name__ == "__main__":
    main()