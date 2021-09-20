def solution(scores):
    answer = ""
    n = len(scores)
    box = [[] for i in range(n)]
    for c in range(n):
        self_score = 0
        for r in range(n):
            if c != r:
                box[c].append(scores[r][c])
            else:
                self_score = scores[r][c]
        if self_score > max(box[c]) or self_score < min(box[c]):
            answer += get_score(sum(box[c]) / (n - 1))
        else:
            answer += get_score((sum(box[c]) + self_score) / n)
    return answer


def get_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"
