def solution(participant, completion):
    map = {}
    
    for i in participant:
        map[i] = map.get(i, 0) + 1
    
    for i in completion:
        map[i] -= 1
        
    for i, j in map.items():
        if j != 0:
            return i