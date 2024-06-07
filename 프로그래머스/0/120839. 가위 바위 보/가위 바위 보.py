def solution(rsp):
    answer = ''
    rsp_win = {"2":"0", "0":"5", "5":"2"}
    for play in rsp:
        answer += rsp_win[play]
    return answer