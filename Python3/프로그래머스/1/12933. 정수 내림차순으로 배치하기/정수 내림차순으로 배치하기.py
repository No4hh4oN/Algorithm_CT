from math import pow

def solution(n):
    answer = 0
    arr = []
    
    while n != 0:
        arr.append(n % 10)
        n = (int)(n / 10)
    new = sorted(arr)
    
    for i in range(len(new)):
        answer += new[i] * pow(10, i)
    
    return answer