def solution(n):
    if n % 2 == 1:
        return sum(2*i - 1 for i in range(1, (n//2)+2))
    else:  
        return sum(4*i*i for i in range(1, (n//2)+1))
