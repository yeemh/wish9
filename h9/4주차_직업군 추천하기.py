def solution(table, languages, preference):
    answer = ''
    sum_list = []
    cor_list = ["SI","CONTENTS","HARDWARE","PORTAL","GAME"]
    for i in table:
        line = list(i.split())
        line.reverse()
        sum = 0
        for language in zip(languages,preference):
            idx = [(k+1) * language[1] for k in range(len(line)) if language[0] == line[k]]
            if idx : sum += idx[0]
        sum_list.append(sum)
    answer_list=[cor for cor in zip(cor_list,sum_list) if cor[1] == max(sum_list)]
    answer_list=sorted(answer_list)
    answer = answer_list[0][0]
    return answer