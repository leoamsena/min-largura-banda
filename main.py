import random


def initialSolution(A, f):
    len_graph = len(A)
    q = [0 for x in range(len_graph+1)]
    s = [0 for x in range(len_graph+1)]
    i = 1
    mark = [False for x in range(len_graph+1)]
    k = random.randint(1, len_graph+1)
    mark[k] = True
    q.insert(1, k)
    ql = 1
    f.insert(k, 1)
    l = 1
    while l < len_graph:
        r = 0
        for i1 in range(1, ql + 1):
            i = q[i1]
            for j1 in range(1, len(A[i])):
                print("i=",i,"j1",j1)
                j = A[i][j1]
                if not mark[j]:
                    r += 1
                    s.insert(r, j)
                    mark.insert(j, True)
        j_ = random.randint(1, ql)
        for jl in range(1, ql):
            j = q[j_]
            l += 1
            f.insert(j, l)
            j_ += 1
            if j_ >= ql - 1:
                j_ = 1
        q = s
        ql = r


A = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [
    1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
f = []
initialSolution(A, f)
