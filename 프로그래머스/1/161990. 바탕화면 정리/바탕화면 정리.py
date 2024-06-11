def solution(wallpaper):
    answer = [0, 50, 0, 0]
    
    for i in range(len(wallpaper)):
        # 시작점(lux) >> 중간에 #이 없는 경우도 확인해야 함
        if "#" in wallpaper[len(wallpaper)-1-i]:
            answer[0] = len(wallpaper)-1-i
        # 끝점(rdx)
        if "#" in wallpaper[i]:
            answer[2] = i + 1
            
        for j in range(len(wallpaper[i])):
            # 시작점(luy)
            if wallpaper[i][j] == "#" and j < answer[1]:
                answer[1] = j
            # 끝점(rdy)
            if wallpaper[i][j] == "#" and j >= answer[3]:
                answer[3] = j+1
                
    return answer