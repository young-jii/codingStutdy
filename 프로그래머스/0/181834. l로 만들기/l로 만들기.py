def solution(myString):
    answer = ''
    # 알파벳 문자열 맵핑
    charstr = 'abcdefghijklnmopqrstuvwxyz'
    charstr_list = list(charstr)
    num_list = [i for i in range(1, 27)]
    map_char = dict(zip(charstr_list, num_list))
    # l 문자의 위치 찾기
    l_num = map_char['l']
    # 주어진 문자열에서 l 이하 모두 l로 치환하기
    for y in myString:
        if map_char[y] < l_num:
            answer += 'l'
        else:
            answer += y
    
    return answer