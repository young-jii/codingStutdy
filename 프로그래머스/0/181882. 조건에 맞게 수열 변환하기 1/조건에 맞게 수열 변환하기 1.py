def solution(arr):
    answer = []
    for i in arr:
        if i % 2 == 1:
            if i < 50:
                answer.append(i * 2)
            else:
                answer.append(i)
        else:
            if i >= 50 :
                answer.append(i / 2)
            else:
                answer.append(i)
    return answer