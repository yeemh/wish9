def solution(weights, head2head):
    answer = []
    record = [[0,0,weights[i],i] for i in range(len(weights))]
    
    for i, result in enumerate(head2head):
        win = result.count('W')
        lose = result.count('L')
        if win != 0:
            record[i][0] = win / (win+lose)
        for j,r in enumerate(result):
            if r == 'W':
                if weights[i] < weights[j]:
                    record[i][1] += 1
                    
    record = sorted(record, key = lambda x: (-x[0], -x[1], -x[2], x[3]))
    
    for _, _, _, i in record:
        answer.append(i+1)
        
    return answer