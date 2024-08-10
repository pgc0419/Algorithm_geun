def solution(numbers):
    answer = []
    length = len(numbers)
    
    for i in range(length):
        for j in range(i + 1, length):
            total = numbers[i] + numbers[j]
            answer.append(total)
    
    answer = list(sorted(set(answer)))
    
    return answer
