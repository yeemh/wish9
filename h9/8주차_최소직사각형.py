def solution(sizes):
    answer = 0
    a=[]
    b=[]
    for w,h in sizes:
        if w>h:
            a.append(w)
            b.append(h)
        else:
            a.append(h)
            b.append(w)    
    answer = max(a) * max(b)
        
    return answer