def solution(todo_list, finished):
    answer = [todo_list[fin] for fin in range(len(finished)) if finished[fin] == False]
    return answer