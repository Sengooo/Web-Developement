def avg(listt):
    sum = 0
    for i in listt:
        sum += i
    return sum/len(listt)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks.keys():
        if i == query_name:
            print(avg(student_marks[i]))