def solution(table, languages, preference):
    score_dict = {}
    score = [5, 4, 3, 2, 1]
    for row in table:
        cur = row.split()
        score_dict[cur[0]] = {}
        for idx, lan in enumerate(cur[1:]):
            score_dict[cur[0]][lan] = score[idx]

    curMax, answer = 0, min(score_dict.keys())
    for job_type, lan_score in score_dict.items():
        cur = 0
        for idx, lan in enumerate(languages):
            # 언어 선호도 * 직업군 언어
            if lan in lan_score:
                cur += lan_score[lan] * preference[idx]
        if cur == curMax:
            answer = min(answer, job_type)
        elif cur > curMax:
            answer = job_type
            curMax = cur
    return answer