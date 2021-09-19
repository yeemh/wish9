def make_dict():
    memo = [[] for i in range(5)]
    memo[0] = ["A", "E", "I", "O", "U"]
    word_dict = ["A", "E", "I", "O", "U"]
    for i in range(4):
        for j in memo[i]:
            for k in memo[0]:
                memo[i + 1].append(j + k)
        word_dict += memo[i + 1]
    return sorted(word_dict)


def solution(word):
    answer = 0
    word_dict = make_dict()
    for cnt, w in enumerate(word_dict):
        if w == word:
            answer = cnt + 1
    return answer