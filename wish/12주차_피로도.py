def dfs(cur_k, dungeons, visited):
    res = 1
    for i in range(len(dungeons)):
        h = 1
        if not visited[i] and cur_k >= dungeons[i][0]:
            visited[i] = True
            h += dfs(cur_k - dungeons[i][1], dungeons, visited)
            visited[i] = False
        res = max(res, h)
    return res


def solution(k, dungeons):
    answer = -1
    dungeons = [x for x in sorted(dungeons, key=lambda x: (-x[0], x[1])) if x[0] <= k]
    visited = [False] * len(dungeons)
    for i in range(len(dungeons)):
        visited[i] = True
        answer = max(answer, dfs(k - dungeons[i][1], dungeons, visited))
        visited[i] = False

    return answer
