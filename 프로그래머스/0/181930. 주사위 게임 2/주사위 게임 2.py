def solution(a, b, c):
    answer = 0
    if a != b != c:
        answer = a + b + c
    if a == b != c or a == c != b or b == c != a:
        answer = (a+b+c)*(a*a+b*b+c*c)
    if a == b == c:
        answer = 27*a*a*a*a*a*a
    return answer