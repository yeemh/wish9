def solution(scores):
    answer = ''
    for i in range(len(scores)):
        my_s=scores[i][i]
        avg=0
        sum_scores=0
        a_list = []
        for j in range(len(scores)):
                sum_scores += scores[j][i]
                a_list.append(scores[j][i])
        if a_list.count(my_s) == 1 and (min(a_list) == my_s or max(a_list) == my_s):
                avg = (sum_scores-my_s) / (len(scores)-1)
        else:
            avg = sum_scores / len(scores)
        
        if avg>=90:
            answer += 'A'
        elif avg>=80:
            answer += 'B'
        elif avg>=70:
            answer += 'C'
        elif avg>=50:
            answer += 'D'
        else:
            answer += 'F'
    return answer