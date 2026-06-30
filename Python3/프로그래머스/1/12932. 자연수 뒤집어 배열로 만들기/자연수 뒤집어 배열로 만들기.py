def solution(n):
    answer = []
    index = 0
    while(n != 0):
        answer.append(n % 10)
        n = (int)(n / 10)
        index+=1
    return answer