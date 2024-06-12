time = input().split(' ')
H = int(time[0])
M = int(time[1])

# 1. 45 - M 이 0보다 클 때
if M - 45 >= 0 :
    # 1-1. 같은 H + 45 - M
    print(str(H) + ' ' + str(M - 45))
elif M - 45 < 0:
    if H == 0:
        H = 24
    print(str(H - 1) + ' ' + str(M - 45 + 60))