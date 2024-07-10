def solution(names):
    answer = []
    len_li = len(names)
    for i in range(len_li):
        if (i+1) % 5 == 1:
            answer.append(names[i])
    return answer