def solution(my_string):
    answer = ''
    moem = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in moem:
            answer += i

    return answer