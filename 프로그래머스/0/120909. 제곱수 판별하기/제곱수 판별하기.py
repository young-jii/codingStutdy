def solution(n):
    answer = 0
    yak = 0
    for i in range(1, n+1, 1):
        if n % i == 0:
            yak += 1
    if yak % 2 == 0:
        answer = 2
    else:
        answer = 1
    return answer