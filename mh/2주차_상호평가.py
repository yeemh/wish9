def solution(scores):
    answer = ''
    n = len(scores) # 사람 수
    average = []
    
    # 배열 뒤집기
    new_scores = list(map(list, zip(*scores)))
    
    for i in range(n):
        max_score = max(new_scores[i]) # 최고점
        min_score = min(new_scores[i]) # 최저점
        # 본인 점수가 최고점이면서 유일한 경우
        if new_scores[i][i] == max_score and new_scores[i].count(max_score) == 1:
            average.append((sum(new_scores[i]) - max_score)/(n-1))
        # 본인 점수가 최저점이면서 유일한 경우
        elif new_scores[i][i] == min_score and new_scores[i].count(min_score) == 1:
            average.append((sum(new_scores[i]) - min_score)/(n-1))
        else:
            average.append(sum(new_scores[i])/n)
            
    for avg_score in average:
        if avg_score >= 90:
            answer += 'A'
        elif 90 > avg_score >= 80:
            answer += 'B'
        elif 80 > avg_score >= 70:
            answer += 'C'
        elif 70 > avg_score >= 50:
            answer += 'D'
        else:
            answer += 'F'
        
    return answer