def solution(a, b):
    answer = 0
    numAB = int(str(a) + str(b))
    numBA = int(str(b) + str(a)) 
    if numAB >= numBA :
        answer = numAB
    else:
        answer = numBA
    return answer