def solution(babbling):
    answer = 0
    speaks = ["aya", "ye", "woo", "ma"]
    
    
    for i in babbling:    
        index = 0
        count = True
        
        while(len(i) > index):
            can = False;
            
            for speak in speaks:
                if i.startswith(speak, index):
                    index += len(speak)
                    can = True;
                    break
            
            if can == False:
                count = False
                break
        if count:
            answer+=1
        
    return answer