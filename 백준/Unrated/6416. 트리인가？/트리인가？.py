import sys
input = sys.stdin.read

def main():
    data = list(map(int, input().split()))
    index = 0
    count = 1

    while index < len(data):
        vertex = dict()
        edge = 0

        while True:
            start = data[index]
            end = data[index + 1]
            index += 2

            if start == -1 and end == -1:
                return
            elif start == 0 and end == 0:
                break

            vertex[start] = vertex.get(start, 0)
            vertex[end] = vertex.get(end, 0) + 1
            edge += 1

        root = 0
        is_tree = True

        for node in vertex:
            if vertex[node] == 0:
                root += 1
            elif vertex[node] > 1:
                is_tree = False
                break

        if len(vertex) == 0:
            print(f"Case {count} is a tree.")
        elif is_tree and root == 1 and edge == len(vertex) - 1:
            print(f"Case {count} is a tree.")
        else:
            print(f"Case {count} is not a tree.")

        count += 1

if __name__ == "__main__":
    main()