def solution(money):
    answer = []
    coffee = money // 5500
    answer.append(coffee)
    answer.append(money - 5500 * coffee)
    return answer