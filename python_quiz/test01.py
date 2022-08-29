# for i in range(1, 11):
#     T = int(input())
#     Text = input().split()
#     T2 = int(input())
#     inin = input().split('I')
#     for i in range(1, T2+1):
#         eof = inin[i].split()
        

foe = ['400905', '139831']
eof = ['1', '6', '436704', '702451', '762737', '557561', '810021', '771706']
foe = foe[:int(eof[0])] + eof[2:] + foe[int(eof[0]):]
foe = foe[:int(eof[0])] + eof[2:] + foe[int(eof[0]):]
print(foe)