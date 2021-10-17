def solution(sizes):
    max_first = -1
    max_second = -1
    
    for size in sizes:
        max_first = max(max_first, max(size))
        max_second= max(max_second, min(size))

    return max_first * max_second
  
