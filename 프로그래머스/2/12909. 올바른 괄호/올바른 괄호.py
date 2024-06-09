def solution(s):
    answer = True

    # [방법2] '('이면 +1, ')'이면 -1 >> 0이면 참, 그 외는 모두 거짓
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False

    if count == 0:
        answer = True
    else: 
        answer = False
        
        
        # [방법1] 순서쌍을 찾음 > 순서쌍이 맞으면 참 [open, close]
        # count = [0, 0]
        # for i in s:
        #     if i == "(":
        #         count[0] += 1
        #     elif i == ")":
        #         count[1] += 1
        # # open 숫자와 close 숫자 값이 같을 때 >> 참
        # if count[0] == count[1]:
        #     answer = True
        # else:
        #     answer = False

    return answer