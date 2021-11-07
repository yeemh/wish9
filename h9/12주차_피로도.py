from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for dungeon in permutations(dungeons):
        cnt = 0
        hp = k
        for i in dungeon:
            if i[0] <= hp:
                hp-=i[1]
                cnt+=1
            else:
                break
        answer = max(answer, cnt)
        if answer == len(dungeons):
            break
    return answer