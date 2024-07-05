right_chess = [1, 1, 2, 2, 2, 8]
white_chess = [int(i) for i in input().split(' ')]
answer = []
for i in range(len(right_chess)):
    answer.append(str(right_chess[i]-white_chess[i]))
print(' '.join(answer))