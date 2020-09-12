# https://j000.tistory.com/30

def solution(array, commands):
    answer = []
    for x in commands:
        i = x[0] - 1
        j = x[1]
        k = x[2]
        
        sorted_array = array[i:j]
        sorted_array.sort()
        answer.append(sorted_array[k-1])

    return answer
