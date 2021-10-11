def solution(weights, head2head):
    answer = []
    n = len(weights)

    # 이긴횟수, 무게가 더 나가는 선수를 이긴 횟수, 몸무게, 번호
    table = [[0] * 4 for i in range(n)]
    fightcnt = [0] * n

    for i in range(n):
        table[i][2], table[i][3] = weights[i], -(i + 1)
        for j in range(i + 1, n):
            if head2head[i][j] != "N":
                fightcnt[i] += 1
                fightcnt[j] += 1
            if head2head[i][j] == "W":
                table[i][0] += 1
                if weights[j] > weights[i]:
                    table[i][1] += 1
            elif head2head[i][j] == "L":
                table[j][0] += 1
                if weights[i] > weights[j]:
                    table[j][1] += 1
        table[i][0] = table[i][0] / fightcnt[i] if fightcnt[i] != 0 else 0

    table.sort(reverse=True)
    answer = [-v[3] for v in table]
    return answer
