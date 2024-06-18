def solution(arr):
    answer = []
    for i in arr:
        for y in range(i):
            answer.append(i)
    
    return answer