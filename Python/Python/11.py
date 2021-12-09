numbers = [10,20,30,40,50,60,70]

print('합', sum(numbers))
print('최대값', max(numbers))
print('카운트', len(numbers))

student_lst = []
students = 5

for i in range(students):
    score = int(input('성적 입력 : '))
    student_lst.append(score)

print('성적 평균 = ', sum(student_lst)/len(student_lst))
print('성적 최대 점수 = ', max(student_lst))