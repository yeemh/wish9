def solution(weights, head2head):
    answer = []
    player = []
    answer1 = [0]*len(weights)
    answer2 = [0]*len(weights)
    for i in range(len(head2head)):
        win=0
        loose=0
        for j in range(len(head2head[i])):
                if head2head[i][j]=='W':
                    win+=1
                    if weights[i] < weights[j]:
                        answer2[i] += 1
                elif head2head[i][j]=='L':
                    loose+=1
        if win >0 or loose>0:
            rate = float(win/(win + loose)) * 100
        else:
            rate = 0
        answer1[i] = rate
    for idx,i in enumerate(zip(answer1,answer2,weights)):
        player.append([i,idx])
    player =sorted(player, key = lambda x : (-x[0][0],-x[0][1],-x[0][2]))
    for i in player:
        print(i)
        answer.append(i[1]+1)
    
    return answer