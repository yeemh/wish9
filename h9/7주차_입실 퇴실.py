def solution(enter, leave):
    answer = []
    room = []
    answer = [0] * (len(enter)+1)
    i=0
    while leave:
        if leave[0] in room:         
            room.remove(leave[0])
            leave.pop(0)
            # print("if")
        else:
            # print("else")
            for j in room:
                answer[j] += 1
            # print("answer :",answer)
            answer[enter[i]] += len(room)
            room.append(enter[i])
            # print("room :",room)
            i+=1
        # print("answer :",answer)
    answer.pop(0)
    return answer