def solution(n_str):
    cnt = 0
    for i in range(len(n_str)):
        if n_str[i] == "0":
            cnt += 1
        else:
            break
    if cnt == 0 :
        answer = n_str
    else:
        answer = n_str[cnt : ]
    return answer