def solution(n):
    # 먼저 1~n 사이에 몇개의 3의 배수, 3이 들어가는게 있는지 생각해야함
    # n을 10으로 나눴을 때 몫이 3이나 나머지가 3이나오는거 , 3의 배수들
    answer = 0
    num = 0

    while num < n:
        answer += 1
        
        if (answer % 3 == 0) or  '3' in str(answer):
            continue
            
        num += 1
    
    return answer