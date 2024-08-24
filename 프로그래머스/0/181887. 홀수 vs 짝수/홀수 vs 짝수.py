def solution(num_list):
    answer = 0
    sum_add = 0
    odd_add = 0
    for i in num_list[::2]:
        sum_add += i
    for j in num_list[1::2]:
        odd_add += j
    if sum_add > odd_add:
        answer = sum_add
    else:
        answer = odd_add
    return answer