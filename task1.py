#!/usr/bin/env python
def markcount():
    if __name__ == '__main__':
        n = int(input("Input count of students: ",))
        student_marks = {}
        for _ in range(n):
            name, *line = input("Input NAME and MARKS separated by a space: ",).split()
            scores = list(map(float, line))
            student_marks[name] = scores
        query_name = input("NAME of student: ",)

    x = sum(student_marks[query_name])/3
    return x



print(markcount())
