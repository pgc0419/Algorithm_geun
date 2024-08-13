def solution(num_list):
    answer1 = 0
    answer2 = 1
    for i in range(len(num_list)):
        answer1 += num_list[i]
        answer2 *= num_list[i]
        
    if answer2 < answer1**2:
        return 1
    else: return 0
