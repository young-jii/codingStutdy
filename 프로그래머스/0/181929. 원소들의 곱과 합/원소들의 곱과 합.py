def solution(num_list):
    answer = 0
    gop = 1
    hap = 0
    
    for i in num_list:
        gop *= i
        hap += i
    if gop < hap*hap:
        answer = 1
    else:
        answer = 0
        
    return answer