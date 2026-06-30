def solution(n):
    answer = 0
    k = n
    while k != 0 :
        answer += (k % 10)
        k =  (int)(k / 10)
    return answer