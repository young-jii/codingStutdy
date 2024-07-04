num_li = input().split()
N = int(num_li[0])
M = int(num_li[1])
origin_num = [i for i in range(1, N+1, 1)]

temp = 0

for i in range(M):
    change_num = input().split()
    temp = origin_num[int(change_num[0])-1]
    origin_num[int(change_num[0])-1] = origin_num[int(change_num[1])-1]
    origin_num[int(change_num[1])-1] = temp
    
answer = [str(y) for y in origin_num]
print(' '.join(answer))