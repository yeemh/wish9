from itertools import product
def solution(word):
    answer = 0
    alpahbet='AEIOU'
    alphabet_dict=[]
    for i in range(1,6):
        for j in product(alpahbet,repeat=i):
            alphabet_dict.append(''.join(j))
    alphabet_dict.sort()
    answer = alphabet_dict.index(word)+1
    return answer