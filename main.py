import random


def initialSolution(A, f):
    len_graph = len(A)
    print("len = ", len_graph)
    q = [0 for x in range(len_graph)]
    s = [0 for x in range(len_graph)]
    i = 1
    mark = [False for x in range(len_graph)]
    k = random.randint(0, len_graph - 1)
    mark[k] = True
    q.insert(0, k)
    ql = 1
    f.insert(k, 0)
    print("f1 = ", f)
    l = 0
    while l < len_graph:
        r = 0
        for i1 in range(ql+1):
            i = q[i1]
            print("i = ", i)
            for j1 in range(len(A[i])):
                j = A[i][j1]
                if not mark[j]:
                    r += 1
                    s.insert(r, j)
                    mark.insert(j, True)
        j_ = random.randint(0, ql)
        for jl in range(0, ql + 1):
            j = q[j_]
            l += 1
            f.insert(j, l)
            print("f2 = ", f)
            j_ += 1
            if j_ >= ql - 1:
                j_ = 0
        q = s
        ql = r


A = [[1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [
    1, 1, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
f = []
initialSolution(A, f)
print("f = ", f)
