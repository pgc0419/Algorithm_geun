def solution(n, control):
    for k in control:
        if k == "w":
            n += 1
        elif k == "s":
            n -= 1
        elif k == "d":
            n += 10
        elif k == "a":
            n -= 10
    
    return n