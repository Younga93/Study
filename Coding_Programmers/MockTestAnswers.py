# https://j000.tistory.com/27

def solution(answers):
    answer = []
    
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    point1 = 0
    point2 = 0
    point3 = 0
    
    for index in range(len(answers)):
        if answers[index] == student1[index % len(student1)]:
            point1 += 1
        if answers[index] == student2[index % len(student2)]:
            point2 += 1
        if answers[index] == student3[index % len(student3)]:
            point3 += 1
    
    highest_point = max(point1, point2, point3)
    
    if highest_point == point1:
        answer.append(1)
    if highest_point == point2:
        answer.append(2)
    if highest_point == point3:
        answer.append(3)
    
    return answer
