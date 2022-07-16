r, g, b = map(int, input().split())
c = (r * g * b)/8/1024/1024
print('%.2f MB' %c)