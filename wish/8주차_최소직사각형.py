def solution(sizes):
    answer = 0
    max_f, max_s = 0, 0
    for w, h in sizes:
        if w >= h:
            max_f, max_s = max(max_f, w), max(max_s, h)
        elif w < h:
            max_f, max_s = max(max_f, h), max(max_s, w)
    answer = max_f * max_s
    return answer
