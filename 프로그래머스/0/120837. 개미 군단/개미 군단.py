def solution(hp):
    answer = 0
    # 병력의 체력
    jang = 5
    byong = 3
    ill = 1
    
    # hp가 병력의 상황에 따라서 달라지는 양상
    if hp >= jang:
        answer += (hp // jang)
        if (hp % jang) >= byong:
            answer += ((hp % jang) // byong)
            answer += (hp % jang % byong)
        else:
            answer += (hp % jang)
    elif hp >= byong:
        answer += (hp // byong)
        answer += (hp % byong)
    else:
        answer += hp
        
    
    return answer