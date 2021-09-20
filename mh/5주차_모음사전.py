def solution(word):
    answer = 0
    word_dic = {"E": 1, "I": 2, "O": 3, "U": 4}
    for i, w in enumerate(word):
        if w == "A":
            answer += 1
        else:
            for j in range(5 - i):
                answer += (5 ** j) * word_dic[w]
            answer += 1
    return answer