numLi = input().split(' ')

M = int(numLi[0])
orginalLi = [ball for ball in range(1, M+1, 1)]

N = int(numLi[1])

for i in range(N):
    switchLi = input().split(' ')
    test_li = orginalLi[int(switchLi[0])-1 : int(switchLi[1])]
    orginalLi = orginalLi[:int(switchLi[0])-1] + test_li[::-1] + orginalLi[int(switchLi[1]):]

a = [str(i) for i in orginalLi]
print(' '.join(a))