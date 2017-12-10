if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores

    query_name = raw_input()
    queryNameList = student_marks.get(query_name)
    print ("{0:.2f}".format(round(reduce(lambda x,y:x+y, queryNameList)/float(len(queryNameList)), 2)))

